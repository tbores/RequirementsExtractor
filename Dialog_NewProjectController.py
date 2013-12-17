'''
Created on 23 mai 2012

@author: tbores
'''

from PySide.QtGui import QDialog, QFileDialog, QMessageBox
from Dialog_NewProjectView import Ui_Dialog_NewProject

class NewProjectController(QDialog):
    '''
    classdocs
    '''
    
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(NewProjectController, self).__init__(parent)
        self.parent = parent
        self.projectName = ''
        self.ui = Ui_Dialog_NewProject()
        self.ui.setupUi(self)
        self.connectButtons()
        self.exec_()
        
    def connectButtons(self):
        '''
        Connect buttons of the dialog
        '''
        self.ui.buttonBox.accepted.connect(self.buttonBox_accepted)
    
    def buttonBox_accepted(self):
        self.projectName = self.ui.lineEdit_ProjectName.text().rstrip().lstrip()
        self.parent.logger.debug('Project Name: \'%s\''%self.projectName)
        
        if self.projectName == '':
            message = 'Project name is empty, please enter a valid project name'
            self.parent.logger.error(message)
            QMessageBox.critical(self,
                                 "Error while adding the file",
                                 message,
                                 QMessageBox.Ok)
