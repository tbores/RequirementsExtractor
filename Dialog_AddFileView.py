# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_AddFile.ui'
#
# Created: Fri Jun 08 15:41:39 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialog_AddFile(object):
    def setupUi(self, dialog_AddFile):
        dialog_AddFile.setObjectName("dialog_AddFile")
        dialog_AddFile.resize(403, 150)
        self.buttonBox = QtGui.QDialogButtonBox(dialog_AddFile)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtGui.QWidget(dialog_AddFile)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 88))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_FilePath = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_FilePath.setObjectName("lineEdit_FilePath")
        self.gridLayout.addWidget(self.lineEdit_FilePath, 1, 0, 1, 1)
        self.toolButton_FilePath = QtGui.QToolButton(self.gridLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/filefind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_FilePath.setIcon(icon)
        self.toolButton_FilePath.setObjectName("toolButton_FilePath")
        self.gridLayout.addWidget(self.toolButton_FilePath, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_Regex = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_Regex.setEditable(True)
        self.comboBox_Regex.setObjectName("comboBox_Regex")
        self.gridLayout.addWidget(self.comboBox_Regex, 3, 0, 1, 1)
        self.fontComboBox = QtGui.QFontComboBox(dialog_AddFile)
        self.fontComboBox.setGeometry(QtCore.QRect(50, 940, 156, 22))
        self.fontComboBox.setObjectName("fontComboBox")

        self.retranslateUi(dialog_AddFile)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dialog_AddFile.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dialog_AddFile.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_AddFile)
        dialog_AddFile.setTabOrder(self.lineEdit_FilePath, self.toolButton_FilePath)
        dialog_AddFile.setTabOrder(self.toolButton_FilePath, self.comboBox_Regex)
        dialog_AddFile.setTabOrder(self.comboBox_Regex, self.buttonBox)
        dialog_AddFile.setTabOrder(self.buttonBox, self.fontComboBox)

    def retranslateUi(self, dialog_AddFile):
        dialog_AddFile.setWindowTitle(QtGui.QApplication.translate("dialog_AddFile", "Add File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialog_AddFile", "File path:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_FilePath.setPlaceholderText(QtGui.QApplication.translate("dialog_AddFile", "D:\\Documents\\MyRequirements.doc", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_FilePath.setText(QtGui.QApplication.translate("dialog_AddFile", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dialog_AddFile", "Regular expression for requirements ID:", None, QtGui.QApplication.UnicodeUTF8))

import qt_resource_file_rc
