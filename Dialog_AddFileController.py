'''
Created on 21 mai 2012

@author: tbores
'''
from PySide.QtGui import QDialog, QFileDialog, QMessageBox
from Dialog_AddFileView import Ui_dialog_AddFile

class AddFileController(QDialog):
    
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(AddFileController, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_dialog_AddFile()
        self.ui.setupUi(self)
        self.filePath = ''
        self.regex = ''
        self.status = False
        self.ui.comboBox_Regex.addItems(self.parent.model.dp_getPreviousRegexList())
        self.connectButtons()
        self.exec_()
        
    def connectButtons(self):
        '''
        Connect buttons of the dialog
        '''
        self.ui.toolButton_FilePath.clicked.connect(self.button_FilePath)
        self.ui.buttonBox.accepted.connect(self.buttonBox_accepted)
        
    def button_FilePath(self):
        self.filePath = QFileDialog.getOpenFileName(self,
                                                   caption="Open MS Word File",
                                                   dir=self.ui.lineEdit_FilePath.text(),
                                                   filter="MS Word Files (*.doc *.docx)")[0]
        self.ui.lineEdit_FilePath.setText(self.filePath)
    
    def buttonBox_accepted(self):
        self.filePath = self.ui.lineEdit_FilePath.text().rstrip().lstrip()
        self.regex = self.ui.comboBox_Regex.currentText()
        self.parent.logger.debug('filePath: %s, regex: %s'%(self.filePath, self.regex))
        
        # Try to update the model
        modelUpdated = self.updateModel()
        
        if modelUpdated != 0:
            if modelUpdated == 1:
                message = 'Regular Expression is empty. Please enter a regular expression.'
            elif modelUpdated == 2:
                message = 'File path is empty. Please give a file.'
            elif modelUpdated == 3:
                message = 'File is already in the project.'
                
            self.parent.logger.error('Error while adding the file: %s'%message)    
            QMessageBox.critical(self,
                                 "Error while adding the file",
                                 message,
                                 QMessageBox.Ok)
        else:
            self.status = True
        
    def updateModel(self):
        self.parent.logger.debug('updateModel')
        ret = 0
        if self.regex != '':
            # Check if regex already present in the previous ones
            alreadyPresent = False
            for regex in self.parent.model.dp_getPreviousRegexList():
                if self.regex == regex:
                    alreadyPresent = True
                    self.parent.logger.debug('Regular expression \'%s\' already in the list of previous reqular expression.', self.regex)
            if alreadyPresent is False:
                self.parent.model.dp_addRegex2PrevRegexList(self.regex)
        
            if self.filePath != '':
                # Check if filepath already present in the fileList
                alreadyPresent = False
                for file in self.parent.model.dp.fileList:
                    if self.filePath == file[0]:
                        alreadyPresent = True
                        self.parent.logger.warn('File already opened.', self.regex)
                        ret = 3
                if alreadyPresent is False:
                    self.parent.model.dp_addFile2FileList([self.filePath, self.regex])
            else:
                ret = 2
        else:
            ret = 1
        return ret
