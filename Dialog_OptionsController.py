'''
Created on 31 mai 2012

@author: tbores
'''

from PySide.QtGui import QDialog
from Dialog_OptionsView import Ui_Dialog_Options

class OptionsController(QDialog):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(OptionsController, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_Dialog_Options()
        self.ui.setupUi(self)
        self.view_updateUiAccordingModel()
        self.connectButtons()
        self.exec_()
       
    def view_updateUiAccordingModel(self):
        self.ui.cbWordShow.setChecked(self.parent.model.dp_getOptions('WordShow'))
        self.ui.cbWordQuit.setChecked(self.parent.model.dp_getOptions('WordQuit'))
        self.ui.cbExcelShow.setChecked(self.parent.model.dp_getOptions('ExcelShow'))
        
    def connectButtons(self):
        '''
        Connect buttons of the dialog
        '''
        self.ui.buttonBox.accepted.connect(self.buttonBox_accepted)
        
    def buttonBox_accepted(self):
        self.parent.model.dp_setOptions('WordShow', self.ui.cbWordShow. isChecked())
        self.parent.model.dp_setOptions('WordQuit', self.ui.cbWordQuit.isChecked())
        self.parent.model.dp_setOptions('ExcelShow', self.ui.cbExcelShow.isChecked())    
        