'''
Created on 22 mai 2012

@author: tbores
'''

import pickle

from Core import MsOfficeHandler
from Core import ErrorHandler

class DataPool(object):
    '''
    The datapool class can be seen as database.
    It contains all the project data.
    Actually when the user save the project, he saves the datapool.
    '''
    def __init__(self, projectName=None):
        '''
        Constructor
        '''
        # fileList is a table of two columns tables
        # [ [fileName_1] [regex_1]
        #   [fileName_2] [regex_2]
        #   ...
        #   [fileName_n] [regex_n] ]
        self.fileList = []
        
        # reqList contains all the requirements
        # It is a table of three columns tables
        # [ [req_1_id] [req_1_version] [req_1_content]
        #  ...  
        #  [req_n_id] [req_n_version] [req_n_content] ]  
        self.reqList = []
        
        self.errorList = []
        
        # previous regex is a list of already used regex for other files
        self.previousRegex = ['REQ-EX-*']
        
        self.projectName = projectName
        
        self.option_WordShow = False
        self.option_WordQuit = True
        self.option_ExcelShow = True

class Model(object):
    '''
    The Model class is responsible for communicating the data to the Controller.
    It's also the interface between the Core and the User Interface(Controller + View)
    '''

    def __init__(self, logger, projectName=None, projectFilePath=None):
        # Create a datapool object that will contains all the project data
        self.dp = DataPool(projectName)
        self.logger = logger
        self.officeHandler = MsOfficeHandler(self, logger)
        self.errorHandler = ErrorHandler(self, logger)
        self.saveStatus = False
        self.observers = []

        self.projectFilePath = ''
        if projectFilePath is not None:
            self.setProjectFilePath(projectFilePath)
        
    def register(self, controller):
        self.observers.append(controller)
            
    def save(self):
        if self.getProjectFilePath() != '':
            with open(self.getProjectFilePath(), 'wb') as f:
                pickle.dump(self.dp, f)
            self.updateSaveStatus(True)
        else:
            self.error('Cannot save project because projectFilePath is empty!')
    
    def load(self):
        if self.getProjectFilePath() != '':
            with open(self.getProjectFilePath(), 'rb') as f:
                self.dp = pickle.load(f)
            self.updateSaveStatus(True)
        else:
            self.logger.error('Cannot load project because projectFilePath is empty!')
        
    def getProjectFilePath(self):
        return self.projectFilePath
    
    def setProjectFilePath(self, path):
        self.projectFilePath = path
    
    def dp_getProjectName(self):
        return self.dp.projectName
    
    def dp_getPreviousRegexList(self):
        return self.dp.previousRegex
    
    def dp_getReqList(self):
        return self.dp.reqList
    
    def dp_getOptions(self, name):
        option = None
        if name == 'WordShow':
            option = self.dp.option_WordShow
        elif name == 'WordQuit':
            option = self.dp.option_WordQuit
        elif name == 'ExcelShow':
            option = self.dp.option_ExcelShow
        
        return option

    def dp_setOptions(self, name, value):
        if name == 'WordShow':
            self.dp.option_WordShow = value
            self.logger.debug('Set option %s to %s'%(name, value))
        elif name == 'WordQuit':
            self.dp.option_WordQuit = value
            self.logger.debug('Set option %s to %s'%(name, value))
        elif name == 'ExcelShow':
            self.dp.option_ExcelShow = value
            self.logger.debug('Set option %s to %s'%(name, value))
        self.updateSaveStatus(False)
        
    def printModel(self):
        print 'Printing Model content:'
        print 'Project: %s'%(self.dp.projectName)
        for file in self.dp.fileList:
            print 'file: %s, regex: %s'%(file[0], file[1])
        for regex in self.dp.previousRegex:
            print 'previous regex: %s'%(regex)
        print 'saveStatus: %s'%(self.saveStatus)
           
    def dp_addFile2FileList(self, coupleFilepathAndRegex):
        self.dp.fileList.append(coupleFilepathAndRegex)
        self.updateSaveStatus(False)
    
    def dp_DelFile2FileList(self, coupleFilepathAndRegex):
        self.dp.fileList.remove(coupleFilepathAndRegex)
        self.updateSaveStatus(False)
        
    def dp_addRegex2PrevRegexList(self, regex):
        self.dp.previousRegex.append(regex)
        self.updateSaveStatus(False)
        
    def dp_addError2ErrorList(self, reqID, errorDescription):
        self.dp.errorList.append([reqID, errorDescription])
        self.updateSaveStatus(False)
        
    def dp_getErrorList(self):
        return self.dp.errorList
    
    def dispatch_ExtractRequirements(self):
        self.dp.reqList = self.officeHandler.extractAllRequirements(self.dp.fileList)
        self.updateSaveStatus(False)
        
    def dispatch_checkErrors(self):
        self.errorHandler.checkErrors()
        
    def dispatch_openFile(self, filePath):
        self.officeHandler.wordOpenFile(filePath)
        
    def dispatch_saveAsExcel(self, filePath):
        self.officeHandler.excelExportRequirements(filePath)
        
    def getSaveStatus(self):
        return self.saveStatus
    
    def updateSaveStatus(self, status):
        if self.getProjectFilePath() != '':
            self.saveStatus = status
            # Notify observer
            self.notifyAll(status)
        
    def notifyAll(self, param):
        for observer in self.observers:
            observer.notify(param)

