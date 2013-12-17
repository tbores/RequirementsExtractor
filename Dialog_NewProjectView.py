# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_NewProject.ui'
#
# Created: Fri Jun 08 15:41:40 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog_NewProject(object):
    def setupUi(self, Dialog_NewProject):
        Dialog_NewProject.setObjectName("Dialog_NewProject")
        Dialog_NewProject.resize(400, 126)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_NewProject)
        self.buttonBox.setGeometry(QtCore.QRect(30, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtGui.QWidget(Dialog_NewProject)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 19, 381, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_ProjectName = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_ProjectName.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_ProjectName.setObjectName("lineEdit_ProjectName")
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lineEdit_ProjectName)

        self.retranslateUi(Dialog_NewProject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_NewProject.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_NewProject.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_NewProject)
        Dialog_NewProject.setTabOrder(self.lineEdit_ProjectName, self.buttonBox)

    def retranslateUi(self, Dialog_NewProject):
        Dialog_NewProject.setWindowTitle(QtGui.QApplication.translate("Dialog_NewProject", "New Project Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_NewProject", "Please enter a project name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ProjectName.setPlaceholderText(QtGui.QApplication.translate("Dialog_NewProject", "Your Project Name", None, QtGui.QApplication.UnicodeUTF8))

