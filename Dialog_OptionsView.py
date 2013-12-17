# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Options.ui'
#
# Created: Fri Jun 08 15:41:40 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog_Options(object):
    def setupUi(self, Dialog_Options):
        Dialog_Options.setObjectName("Dialog_Options")
        Dialog_Options.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Options)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtGui.QTabWidget(Dialog_Options)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtGui.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 7, 361, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.cbWordShow = QtGui.QCheckBox(self.formLayoutWidget)
        self.cbWordShow.setObjectName("cbWordShow")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.cbWordShow)
        self.cbExcelShow = QtGui.QCheckBox(self.formLayoutWidget)
        self.cbExcelShow.setChecked(True)
        self.cbExcelShow.setObjectName("cbExcelShow")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.cbExcelShow)
        self.cbWordQuit = QtGui.QCheckBox(self.formLayoutWidget)
        self.cbWordQuit.setChecked(True)
        self.cbWordQuit.setObjectName("cbWordQuit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.cbWordQuit)
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog_Options)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_Options.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_Options.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Options)

    def retranslateUi(self, Dialog_Options):
        Dialog_Options.setWindowTitle(QtGui.QApplication.translate("Dialog_Options", "Requirements Extractor Options", None, QtGui.QApplication.UnicodeUTF8))
        self.cbWordShow.setText(QtGui.QApplication.translate("Dialog_Options", "Show Microsoft Word file during extraction", None, QtGui.QApplication.UnicodeUTF8))
        self.cbExcelShow.setText(QtGui.QApplication.translate("Dialog_Options", "Show ouput Microsoft Excel file", None, QtGui.QApplication.UnicodeUTF8))
        self.cbWordQuit.setText(QtGui.QApplication.translate("Dialog_Options", "Quit Microsoft Word after extraction", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog_Options", "MS Office", None, QtGui.QApplication.UnicodeUTF8))

