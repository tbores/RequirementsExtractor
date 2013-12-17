'''
Created on 23 mai 2012

@author: tbores
'''

import pythoncom
import win32com.client
import re
import logging

from time import sleep

WORD_END_CELL_SEPARATOR = u'\r\x07'
REGEX_PARENTHESIS_NUMBER = '\([0-9]+\)'

class ErrorHandler(object):
    
    def __init__(self, model, logger):
        self.model = model
        self.logger = logger
    
    def checkErrors(self):
        duplicatedReqID = self.checkDuplicatedReqID()
        for req in duplicatedReqID:
            self.model.dp_addError2ErrorList(req, 'Duplicated requirement')
            
    def checkDuplicatedReqID(self):
        duplicatedReqID = []
    # Go through the requirement list and check every Req ID
        for req in self.model.dp_getReqList():
            isReqIDAlreadyChecked = False
            counter = 0;
    # Check if this ID is already marked as duplicated
            for reqID in duplicatedReqID:
                if req[0] == reqID:
                    isReqIDAlreadyChecked = True
    # If the current req ID isn't marked as duplicated compare it to all others req ID
            if isReqIDAlreadyChecked == False:
                for req2 in self.model.dp_getReqList():
                    if req[0] == req2[0]:
                        counter += 1
                        if counter > 1:
                            duplicatedReqID.append(req[0])
                            self.logger.error("Requirement ID: " + req[0]+ " is duplicated.")
    
        if len(duplicatedReqID) < 1:
            self.logger.debug("No duplicated requirement ID found, good!")
    
        return duplicatedReqID

class MsOfficeHandler(object):
    '''
    classdocs
    '''

    def __init__(self, model, logger):
        '''
        Constructor
        '''
        self.logger = logger
        self.model = model
       
    def wordOpenFile(self, filePath):
        word = win32com.client.DispatchEx('Word.Application', clsctx = pythoncom.CLSCTX_LOCAL_SERVER)
        doc = word.Documents.Open(filePath, ReadOnly=False)
        word.Visible = True
        sleep(1)
        
    def extractAllRequirements(self, fileList):
        self.logger.debug('Extracting all requirement')
        reqList = []
        # Start Microsoft Word, open the file and hide word
        self.logger.debug("Starting Microsoft Word...")
#        word = win32.gencache.EnsureDispatch('Word.Application')
        word = win32com.client.DispatchEx('Word.Application', clsctx = pythoncom.CLSCTX_LOCAL_SERVER)
        
        for file in fileList:
            self.wordFileExtractRequirements(word, file, reqList)
            
        if self.model.dp_getOptions('WordQuit'):
            word.Application.Quit()
            
        self.logger.debug("Exporting requirements from the word file: done.")
        return reqList
        
    def wordFileExtractRequirements(self, word, coupleFilepathAndRegex, reqList):
        doc = word.Documents.Open(coupleFilepathAndRegex[0], ReadOnly=True)
        word.Visible = self.model.dp_getOptions('WordShow')
        sleep(1)

        # Parse all tables in word document and look if it contains a requirement
        # Save the founded requirement in a table structure in memory
        for table in doc.Tables:
            for i in range(1, table.Rows.Count+1):
                cellContent = unicode(table.Cell(i, 1)).rstrip(WORD_END_CELL_SEPARATOR).rstrip().lstrip()
                if re.match(coupleFilepathAndRegex[1], cellContent):
                    reqID = re.sub(REGEX_PARENTHESIS_NUMBER, '', cellContent) # Extract Requirement ID
                    if len(re.findall(REGEX_PARENTHESIS_NUMBER, cellContent)) > 0:
                        reqVersion = unicode(re.findall(REGEX_PARENTHESIS_NUMBER, cellContent)[0]).lstrip('(').rstrip(')') # Extract Requirement version
                    else:
                        reqVersion = 'None'
                    if table.Columns.Count > 1:
                        reqContent = unicode(table.Cell(i,2)).rstrip(WORD_END_CELL_SEPARATOR).rstrip().lstrip() # Extract requirement content
                        reqList.append([reqID, reqVersion, reqContent])
                    else:
                        self.logger.debug("Requirement "+reqID+" has NO content")
                i += 1
        # Close document and quit Microsoft Word
        doc.Close(0, 1) # 0 = do not saved changes, 1 = original format

    def excelExportRequirements(self, filePath):
        self.logger.debug('excelExportRequirements')
        # Start Microsoft Excel, create a new file
#        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel = win32com.client.DispatchEx('Excel.Application', clsctx = pythoncom.CLSCTX_LOCAL_SERVER)
    
        # Add a new sheet and save requirements in it
        xls = excel.Workbooks.Add()
        ws = xls.ActiveSheet
        ws.Name = "Requirements List"
        excel.Visible = self.model.dp_getOptions('ExcelShow')
        sleep(1)
    
        i = 1;
        for req in self.model.dp_getReqList():
            ws.Cells(i, 1).Value = req[0]
            ws.Cells(i, 2).Value = req[1]
            ws.Cells(i, 3).Value = req[2]
            i += 1
        # Add a new sheet and save the duplicated req ID in it.
        ws = xls.Sheets(2)
        ws.Name = "Errors"
        
        if len(self.model.dp_getErrorList()) > 0:
            i = 1
            for error in self.model.dp_getErrorList():
                ws.Cells(i, 1).Value = error[0]
                ws.Cells(i, 2).Value = error[1]
                i += 1
    
        # Save file, close it and quit excel
        xls.SaveAs(filePath)
        
        if self.model.dp_getOptions('ExcelShow') is False:
            xls.Close()
            excel.Application.Quit()