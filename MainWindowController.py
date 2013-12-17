'''
Created on 21 mai 2012

@author: Thomas Bores
'''

import os
import sys
import platform
import PySide
import re

from PySide.QtCore import *
from PySide.QtGui import *

from Model import Model
from MainWindowView import Ui_MainWindow
from Dialog_AddFileController import AddFileController
from Dialog_NewProjectController import NewProjectController
from Dialog_OptionsController import OptionsController

class MainWindowController(QMainWindow):
    '''
    classdocs
    '''

    def __init__(self, version=None, year=None, parent=None, logger=None):
        '''
        Constructor
        '''
        self.version = version
        self.year = year
        self.logger = logger
        self.model = None
        super(MainWindowController, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectButtons()
        self.setWindowTitle('ReqExtractor: No Project')
        
    def connectButtons(self):
        '''
        Menu
        '''
        # File
        self.ui.action_NewProject.triggered.connect(self.action_NewProject)
        self.ui.action_OpenProject.triggered.connect(self.action_OpenProject)
        self.ui.action_SaveProject.triggered.connect(self.action_SaveProject)
        self.ui.action_SaveProjectAs.triggered.connect(self.action_SaveProjectAs)
        self.ui.action_AddFile.triggered.connect(self.action_AddFile)
        self.ui.action_DelFile.triggered.connect(self.action_DelFile)
        self.ui.action_ExportRequirementsAsExcelFile.triggered.connect(self.action_ExportRequirementsAsExcelFile)
        self.ui.action_Quit.triggered.connect(self.action_Quit)
        # Tools
        self.ui.action_ExtractRequirements.triggered.connect(self.action_ExtractRequirements)
        self.ui.action_CheckForErrors.triggered.connect(self.action_CheckForErrors)
        self.ui.action_Options.triggered.connect(self.action_Options)
        # Help
        self.ui.action_AboutReqExt.triggered.connect(self.action_AboutReqExt)
        self.ui.action_AboutPlatform.triggered.connect(self.action_AboutPlatform)
        # GroupBox 'Project Files'
        self.ui.toolButton_AddFile.clicked.connect(self.action_AddFile)
        self.ui.toolButton_DelFile.clicked.connect(self.action_DelFile)
        self.ui.toolButton_OpenFile.clicked.connect(self.action_OpenFile)
        self.ui.treeWidget.itemDoubleClicked.connect(self.action_OpenFile)
        # TabWidget
        self.ui.lineEdit_ReqIDFilter.textChanged.connect(self.lineEdit_ReqFilter)
        self.ui.lineEdit_ReqContentFilter.textChanged.connect(self.lineEdit_ReqFilter)
        
    def action_NewProject(self):
        self.logger.debug('action_NewProject')
        if self.saveProjectDialog() == True:
            self.view_resetUi()
            dlg = NewProjectController(parent=self)
            if dlg.projectName != '':
                self.model = Model(logger=self.logger, projectName=dlg.projectName)
                self.model.register(self)
                self.view_setTitle(self.model.dp_getProjectName()+' *')
                self.view_updateUiAfterProjectLoad()
    
    def action_OpenProject(self):
        self.logger.debug('action_OpenProject')
        if self.saveProjectDialog() == True:
            self.view_resetUi()
            projectFile = QFileDialog.getOpenFileName(self,
                                                           caption='Open project',
                                                           dir=os.curdir,
                                                           filter="Requirement Extractor Project File (*.pkl)")[0]
            if projectFile != '':
                self.model = Model(logger=self.logger, projectFilePath=projectFile)
                self.model.load()
                self.model.printModel()
                self.model.register(self)
                self.view_setTitle(self.model.dp_getProjectName())
                self.view_updateUiAfterProjectLoad()

    def action_SaveProject(self):
        self.logger.debug('action_SaveProject')
        self.model.save()
            
    def action_SaveProjectAs(self):
        self.logger.debug('action_SaveProjectAs')
        projectFile = QFileDialog.getSaveFileName(self,
                                                       caption="Save project as",
                                                       dir=os.curdir,
                                                       filter="Requirement Extractor Project File (*.pkl)")[0]
        self.model.setProjectFilePath(projectFile)
        self.model.save()
        
    def action_AddFile(self):
        self.logger.debug('action_AddFile')
        dlg = AddFileController(parent=self)
        if dlg.status is True:
            self.view_addFileInTree([dlg.filePath, dlg.regex])
            
    def action_DelFile(self):
        self.logger.debug('action_DelFile')
        coupleFilepathAndRegex = self.view_delFileInTree()
        if coupleFilepathAndRegex is not None:
            self.logger.debug('Remove %s from Model Datapool'%(coupleFilepathAndRegex))
            self.model.dp_DelFile2FileList(coupleFilepathAndRegex)
    
    def action_ExportRequirementsAsExcelFile(self):
        self.logger.debug('action_ExportRequirementsAsExcelFile')
        ret = QFileDialog.getSaveFileName(self,
                                          caption="Export Requirements in an Excel File",
                                          dir=None,
                                          filter="MS Excel Files (*.xls, *.xlsx)")[0]
        self.model.dispatch_saveAsExcel(ret)
    
    def action_Quit(self):
        self.logger.debug('action_Quit')
        if self.saveProjectDialog() is True:
            sys.exit()
    
    def action_ExtractRequirements(self):
        self.logger.debug('action_ExtractRequirements')
        self.ui.tabWidget.setCurrentIndex(0)
        self.model.dispatch_ExtractRequirements()
        self.view_updateReqTable()
       
    def action_CheckForErrors(self):
        self.logger.debug('action_CheckForErrors')
        self.ui.tabWidget.setCurrentIndex(1)
        self.model.dispatch_checkErrors()
        self.view_updateErrorTable()
        
    def action_Options(self):
        self.logger.debug('action_Options')
        OptionsController(parent=self)
        
    def action_AboutPlatform(self):
        self.logger.debug('action_AboutPlatform')
        QMessageBox.about(self, 'About Platform',
                          """<p>Python %s -  PySide version %s - Qt version %s on %s"""% \
                          (platform.python_version(), PySide.__version__,\
                           PySide.QtCore.__version__, platform.system())
                          )
       
    def action_AboutReqExt(self):
        self.logger.debug('action_AboutReqExt')
        QMessageBox.about(self, 'About Requirements Extractor', 
                          """<b>Requirements Extractor v%s</b>
                          <p>Copyright (c) %s, Thomas Bores. All rights reserved according GPL v2.</p>"""%(self.version, self.year)
                          )
    
    def action_OpenFile(self):
        self.logger.debug('action_OpenFile')
        if len(self.ui.treeWidget.selectedItems()) > 0 and self.ui.treeWidget.itemAt(0, 0).isSelected() == False:
            for i in range(0, self.ui.treeWidget.itemAt(0, 0).childCount()):
                if self.ui.treeWidget.itemAt(0, 0).child(i).isSelected():
                    self.model.dispatch_openFile(self.ui.treeWidget.itemAt(0, 0).child(i).text(0))
    
    def lineEdit_ReqFilter(self):
        self.logger.debug('lineEdit_ReqFilter')
        
        reqIdRegEx = None
        reqContentRegEx = None
        
        reqIdFilter = self.ui.lineEdit_ReqIDFilter.text().rstrip().lstrip()
        reqContentFilter = self.ui.lineEdit_ReqContentFilter.text().rstrip().lstrip()
        
        if reqIdFilter != '':
            reqIdRegEx = re.compile(reqIdFilter)
        if reqContentFilter != '':
            reqContentRegEx = re.compile(reqContentFilter)
            
        self.view_updateReqTable(reqIdFilter=reqIdRegEx, reqContentFilter=reqContentRegEx)
                
    def view_addFileInTree(self, coupleFileAndRegex):
        self.logger.debug('view_addFileInTree')
        # Update View
        icon = QIcon()
        icon.addPixmap(QPixmap(":/Pixmap/ico/16x16/filesystems/file_doc.png"), QIcon.Normal, QIcon.Off)
        projectItem = self.ui.treeWidget.itemAt(0, 0)
        wItem = QTreeWidgetItem(projectItem)
        wItem.setIcon(0, icon)
        wItem.setText(0, coupleFileAndRegex[0])
        wItem.setText(1, coupleFileAndRegex[1])

    def view_delFileInTree(self):
        self.logger.debug('view_delFileInTree')
        if len(self.ui.treeWidget.selectedItems()) > 0 and self.ui.treeWidget.itemAt(0, 0).isSelected() == False:
            for i in range(0, self.ui.treeWidget.itemAt(0, 0).childCount()):
                if self.ui.treeWidget.itemAt(0, 0).child(i).isSelected():
                    coupleFilepathAndRegex = ['', '']
                    coupleFilepathAndRegex[0] = self.ui.treeWidget.itemAt(0, 0).child(i).text(0)
                    coupleFilepathAndRegex[1] = self.ui.treeWidget.itemAt(0, 0).child(i).text(1)
                    self.ui.treeWidget.itemAt(0, 0).takeChild(i)
                    return coupleFilepathAndRegex
                else:
                    i += 1
        else:
            QMessageBox.warning(self,
                                'No file selected',
                                ('No file selected.\n' + \
                                'Please select a file to remove!'),
                                QMessageBox.Ok)
        return None

    def view_updateUiAfterProjectLoad(self):
        self.logger.debug('view_updateUiAfterProjectLoad')
        self.view_setEnabled(True)
        self.ui.treeWidget.itemAt(0, 0).setText(0, self.model.dp_getProjectName())
        # Load files
        for file in self.model.dp.fileList:
            self.view_addFileInTree(file)
        # Load requirements
        self.view_updateReqTable()
        self.view_updateErrorTable()
    
    def view_setEnabled(self, state):
        self.logger.debug('view_setEnabled')
        # File
        self.ui.action_SaveProjectAs.setEnabled(state)
        self.ui.menuProject.setEnabled(state)
        self.ui.action_AddFile.setEnabled(state)
        self.ui.action_DelFile.setEnabled(state)
        self.ui.action_OpenFile.setEnabled(state)
        self.ui.menuExport.setEnabled(state)
        self.ui.action_ExportRequirementsAsExcelFile.setEnabled(state)
        # Tools
        self.ui.action_ExtractRequirements.setEnabled(state)
        self.ui.action_ExtractFlows.setEnabled(state)
        self.ui.action_CheckForErrors.setEnabled(state)
        self.ui.action_Options.setEnabled(state)
        # MainWindow component
        self.ui.tabWidget.setEnabled(state)
        self.ui.tableWidget.setEnabled(state)
        # dockWidget
        self.ui.dockWidget_ProjectFiles.setEnabled(state)
        self.ui.toolButton_AddFile.setEnabled(state)
        self.ui.toolButton_DelFile.setEnabled(state)
        self.ui.toolButton_OpenFile.setEnabled(state)
        self.ui.treeWidget.setEnabled(state)
        self.ui.treeWidget.itemAt(0, 0).setDisabled(not state)
    
    def view_resetUi(self):
        self.logger.debug('view_resetUi')
        self.view_cleanTable(self.ui.tableWidget)
        self.view_cleanTable(self.ui.tableWidget_Errors)
        self.view_cleanFileTree()
        self.view_setEnabled(False)
        self.setWindowTitle('ReqExtractor: No Project')
        self.ui.treeWidget.itemAt(0, 0).setText(0, 'Project')
            
    def view_updateReqTable(self, reqIdFilter=None, reqContentFilter=None):
        self.logger.debug('view_updateReqTable')
        row = 0
        self.view_cleanTable(self.ui.tableWidget)
        
        for req in self.model.dp_getReqList():
            if reqIdFilter is None and reqContentFilter is None:
                self.view_updateTableRow(row, req, self.ui.tableWidget)
                row += 1
            elif reqIdFilter is not None and reqContentFilter is not None:
                if reqIdFilter.search(req[0]) is not None:
                    if reqContentFilter.search(req[2]) is not None:
                        self.view_updateTableRow(row, req, self.ui.tableWidget)
                        row += 1
            elif reqIdFilter is not None and reqContentFilter is None:
                if reqIdFilter.search(req[0]) is not None:
                    self.view_updateTableRow(row, req, self.ui.tableWidget)
                    row += 1
            elif reqIdFilter is None and reqContentFilter is not None:
                if reqContentFilter.search(req[2]) is not None:
                    self.view_updateTableRow(row, req, self.ui.tableWidget)
                    row += 1
                
    def view_updateErrorTable(self):
        self.logger.debug('view_updateErrorTable')
        self.view_cleanTable(self.ui.tableWidget_Errors)
        row = 0
        for error in self.model.dp_getErrorList():
            self.view_updateTableRow(row, error, self.ui.tableWidget_Errors)
            row += 1
        
    def view_updateTableRow(self, row, content, tableObject):
        column = 0
        if row >= tableObject.rowCount():
            tableObject.insertRow(tableObject.rowCount())
        for cell in content:
            item = QTableWidgetItem()
            item.setText(cell)
            tableObject.setItem(row, column, item)
            column += 1
            
    def view_cleanTable(self, tableObject):
        tableObject.clearContents()
        numOfRow =  tableObject.rowCount()
        for row in range(numOfRow):
            tableObject.removeRow(tableObject.rowCount()-1)
    
    def view_cleanFileTree(self):
        childs = self.ui.treeWidget.itemAt(0, 0).childCount()
        for i in range(0, childs):
            self.ui.treeWidget.itemAt(0, 0).takeChild(i)
        
    def view_setTitle(self, txt):
        self.setWindowTitle('ReqExtractor: '+txt)
    
    def notify(self, status):
        if status:
            self.view_setTitle(self.model.dp_getProjectName())
            self.ui.action_SaveProject.setEnabled(False)
        else :
            self.view_setTitle(self.model.dp_getProjectName()+' *')
            self.ui.action_SaveProject.setEnabled(True)

    def saveProjectDialog(self):
        self.logger.debug('saveProjectDialog')
        if self.model is not None and self.model.getSaveStatus() == False:
            ret = QMessageBox.question(self,
                                       'Current project not saved',
                                       ('The project has been modified.\n' + \
                                        'Do you want to save your changes?'),
                                        QMessageBox.Save | QMessageBox.Discard| QMessageBox.Cancel,
                                        QMessageBox.Save)
            if ret == QMessageBox.Save:
                if self.model.getProjectFilePath() != '':
                    self.model.save()
                else:
                    self.action_SaveProjectAs()
                return True
            elif ret == QMessageBox.Discard:
                return True
            else:
                return False
        else:
            return True
        
    def view_error(self, title, msg):
        self.logger.error('%s: %s'%title, msg)
        QMessageBox.critical(self, title, msg, QMessageBox.Ok)
