#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) Thomas Bores (http://blog.bores.fr)

from time import sleep
import win32com.client as win32
import re
import pickle
import os
import traceback
import pythoncom
import win32com.client

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

# Import UI class
from req_extractor_ui import Ui_Dialog

# Constants
WORD_END_CELL_SEPARATOR = u'\r\x07'
REGEX_PARENTHESIS_NUMBER = '\([0-9]+\)'

class ReqExtController(QDialog):

    modelFilePath = './req_extractor_model.pkl'
    model = {'inFile':'', 'regex':'', 'outFile':''}
    
    def __init__(self, parent=None):
        super(ReqExtController, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.bInputDoc.clicked.connect(self.bInputDocClicked)
        self.ui.bOutputDoc.clicked.connect(self.bOutputDocClicked)
        self.ui.bExtractReq.clicked.connect(self.bExtractReqClicked)
        
        # If a configuration file is found, we fill the input fields
        if os.path.isfile(self.modelFilePath):
            self.setText('UI config file found.')
            with open(self.modelFilePath, 'rb') as f:
                self.model = pickle.load(f)
                self.ui.leInputDocPath.setText(unicode(self.model['inFile']))
                self.ui.leRegex.setText(unicode(self.model['regex']))
                self.ui.leOutputDocPath.setText(unicode(self.model['outFile']))
        else: # It seems it is the first time the user launch the program, we auto configure the input with the provided examples
            if os.path.isfile(os.getcwd()+'/examples/RequirementsExample.doc'):
                self.ui.leInputDocPath.setText(unicode(os.getcwd()+'/examples/RequirementsExample.doc'))
                self.ui.leRegex.setText(unicode('REQ-EX-*'))
                self.ui.leOutputDocPath.setText(unicode(os.getcwd()+'/examples/exported_RequirementsExample.xls'))
        
    def saveModel(self):
        with open(self.modelFilePath, 'wb') as f:
            pickle.dump(self.model, f)
        
    def setText(self, txt):
        self.ui.textBrowser.append(txt)
        self.ui.textBrowser.repaint()
        print txt
    
    def setProgress(self, percentage):
        self.ui.progressBar.setValue(percentage)
        
    def parseUserInput(self, path):
        path = path.strip()
        path = path.strip('\n')
        path = path.strip('\r')
        path = path.strip()
        return path

    def bInputDocClicked(self):
        self.model['inFile'] = QFileDialog.getOpenFileName(self,
                                                   caption="Open MS Word File",
                                                   dir=self.ui.leInputDocPath.text(),
                                                   filter="MS Word Files (*.doc *.docx)")[0]
        self.ui.leInputDocPath.setText(self.model['inFile'])
        self.saveModel()

    def bOutputDocClicked(self):
        self.model['outFile'] = QFileDialog.getSaveFileName(self,
                                                    caption="Save MS Excel File",
                                                    dir=self.ui.leOutputDocPath.text(),
                                                    filter="MS Excel Files (*.xls, *.xlsx)")[0]
        self.ui.leOutputDocPath.setText(self.model['outFile'])
        self.saveModel()
    
    def bExtractReqClicked(self):
        self.model['inFile'] = self.parseUserInput(self.ui.leInputDocPath.text())
        self.model['regex'] = self.parseUserInput(self.ui.leRegex.text())
        self.model['outFile'] = self.parseUserInput(self.ui.leOutputDocPath.text())
        self.saveModel()
        
        if  self.model['regex'] != "":
            if self.model['inFile'] != "":
                if self.model['outFile'] != "":
                    run(self)
                else:
                    self.ui.textBrowser.setText("Please enter an output excel file.")
                    QMessageBox.critical(self,
                                      "Ouput excel file empty",
                                      "No output excel file.\n" + \
                                      "Please choose an excel file.",
                                      QMessageBox.Ok)
            else:
                self.setText("Please enter an input word file.")
                QMessageBox.critical(self,
                                  "Input word file empty",
                                  "No input word file.\n" + \
                                  "Please choose a word file.",
                                  QMessageBox.Ok)
        else:
            self.setText("Please enter requirement ID regular expression")
            QMessageBox.critical(self,
                              "Regular Expression empty",
                              "No regular expression for requirement ID has been written\n" + \
                              "Program cannot extracts requirement without that!",
                              QMessageBox.Ok)

class ReqExtCore:
        
    def __init__(self, controller):
        self.controller = controller
        self.reqList = []
        
    def checkDuplicateReqID(self):
        self.controller.setText("Checking for duplicated requirements ID...")
        duplicatedReqID = []
    # Go through the requirement list and check every Req ID
        for req in self.reqList:
            isReqIDAlreadyChecked = False
            counter = 0;
    # Check if this ID is already marked as duplicated
            for reqID in duplicatedReqID:
                if req[0] == reqID:
                    isReqIDAlreadyChecked = True
    # If the current req ID isn't marked as duplicated compare it to all others req ID
            if isReqIDAlreadyChecked == False:
                for req2 in self.reqList:
                    if req[0] == req2[0]:
                        counter += 1
                        if counter > 1:
                            duplicatedReqID.append(req[0])
                            self.controller.setText("Requirement ID: " + req[0]+ " is duplicated.")
    
        if len(duplicatedReqID) < 1:
            self.controller.setText("No duplicated requirement ID found, good!")
    
        self.controller.setText("Checking for duplicated requirements ID: done.")
        return duplicatedReqID
    
    def wordExtractRequirements(self):
        self.controller.setText("Starting Microsoft Word...")
    # Start Microsoft Word, open the file and hide word
#        word = win32.gencache.EnsureDispatch('Word.Application')
        word = win32com.client.DispatchEx('Word.Application', clsctx = pythoncom.CLSCTX_LOCAL_SERVER)
        doc = word.Documents.Open(self.controller.model['inFile'], ReadOnly=True)
        word.Visible = self.controller.ui.cbWordShow.isChecked()
        sleep(1)
    
    # Parse all tables in word document and look if it contains a requirement
    # Save the founded requirement in a table structure in memory
        self.controller.setText("Exporting requirements from the word file "+self.controller.model['inFile']+"...")
        counter = 1
        for table in doc.Tables:
            self.controller.setProgress(50*counter/len(doc.Tables))
            counter += 1
            for i in range(1, table.Rows.Count+1):
                cellContent = unicode(table.Cell(i, 1)).rstrip(WORD_END_CELL_SEPARATOR).rstrip().lstrip()
                if re.match(self.controller.model['regex'], cellContent):
                    reqID = re.sub(REGEX_PARENTHESIS_NUMBER, '', cellContent) # Extract Requirement ID
                    reqVersion = unicode(re.findall(REGEX_PARENTHESIS_NUMBER, cellContent)[0]).lstrip('(').rstrip(')') # Extract Requirement version
                    if table.Columns.Count > 1:
                        reqContent = unicode(table.Cell(i,2)).rstrip(WORD_END_CELL_SEPARATOR).rstrip().lstrip() # Extract requirement content
                        self.reqList.append([reqID, reqVersion, reqContent])
                    else:
                        self.controller.setText("Requirement "+reqID+" has NO content")
                i += 1
    
    # Close document and quit Microsoft Word

        doc.Close(0, 1) # 0 = do not saved changes, 1 = original format
        if self.controller.ui.cbWordQuit is True:
            word.Application.Quit()
        self.controller.setText("Exporting requirements from the word file: done.")
    
    def excelExportRequirements(self):
        self.controller.setText("Starting Microsoft Excel...")
    # Start Microsoft Excel, create a new file
#        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel = win32com.client.DispatchEx('Excel.Application', clsctx = pythoncom.CLSCTX_LOCAL_SERVER)
    
    # Add a new sheet and save requirements in it
        self.controller.setText("Writing requirements in Excel file "+self.controller.model['outFile']+"...")
        xls = excel.Workbooks.Add()
        ws = xls.ActiveSheet
        ws.Name = "Requirements List"
        excel.Visible = self.controller.ui.cbExcelShow.isChecked()
        sleep(1)
    
        i = 1;
        for req in self.reqList:
            self.controller.setProgress(50+(i*50/len(self.reqList)))
            ws.Cells(i, 1).Value = req[0]
            ws.Cells(i, 2).Value = req[1]
            ws.Cells(i, 3).Value = req[2]
            i += 1
    # Add a new sheet and save the duplicated req ID in it.
        ws = xls.Sheets(2)
        ws.Name = "Errors"
        duplicatedReqID = self.checkDuplicateReqID()
        if len(duplicatedReqID) > 0:
            i = 1
            for reqID in duplicatedReqID:
                ws.Cells(i, 1).Value = reqID
                ws.Cells(i, 2).Value = "Requirement ID duplicated"
                i += 1
    
    # Save file, close it and quit excel
        xls.SaveAs(self.controller.model['outFile'])
        
        if self.controller.ui.cbExcelShow.isChecked() is False:
            xls.Close()
            excel.Application.Quit()
        self.controller.setText("Writing requirements in Excel file: done.")

def run(controller):
    controller.setProgress(0)
    core = ReqExtCore(controller)
    core.wordExtractRequirements()
    controller.setProgress(50)
    core.excelExportRequirements()
    controller.setProgress(100)        
    controller.setText("Requirements extraction done.")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    dialog = ReqExtController()
    dialog.show()
    # Run the run Qt loop
    sys.exit(app.exec_())
