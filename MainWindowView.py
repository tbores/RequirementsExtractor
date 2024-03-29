# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri Jun 08 15:41:39 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabReq = QtGui.QWidget()
        self.tabReq.setObjectName("tabReq")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabReq)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_ReqIDFilter = QtGui.QLineEdit(self.tabReq)
        self.lineEdit_ReqIDFilter.setObjectName("lineEdit_ReqIDFilter")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_ReqIDFilter)
        self.label_2 = QtGui.QLabel(self.tabReq)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_ReqContentFilter = QtGui.QLineEdit(self.tabReq)
        self.lineEdit_ReqContentFilter.setObjectName("lineEdit_ReqContentFilter")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_ReqContentFilter)
        self.label = QtGui.QLabel(self.tabReq)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tableWidget = QtGui.QTableWidget(self.tabReq)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tabReq, "")
        self.tabErrors = QtGui.QWidget()
        self.tabErrors.setObjectName("tabErrors")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabErrors)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget_Errors = QtGui.QTableWidget(self.tabErrors)
        self.tableWidget_Errors.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Errors.setObjectName("tableWidget_Errors")
        self.tableWidget_Errors.setColumnCount(2)
        self.tableWidget_Errors.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Errors.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Errors.setHorizontalHeaderItem(1, item)
        self.tableWidget_Errors.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_Errors.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget_Errors.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.tableWidget_Errors)
        self.tabWidget.addTab(self.tabErrors, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menuFile.setObjectName("menuFile")
        self.menuProject = QtGui.QMenu(self.menuFile)
        self.menuProject.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuProject.setIcon(icon)
        self.menuProject.setObjectName("menuProject")
        self.menuExport = QtGui.QMenu(self.menuFile)
        self.menuExport.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/db_comit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuExport.setIcon(icon1)
        self.menuExport.setObjectName("menuExport")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_ProjectFiles = QtGui.QDockWidget(MainWindow)
        self.dockWidget_ProjectFiles.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_ProjectFiles.sizePolicy().hasHeightForWidth())
        self.dockWidget_ProjectFiles.setSizePolicy(sizePolicy)
        self.dockWidget_ProjectFiles.setMaximumSize(QtCore.QSize(524287, 200))
        self.dockWidget_ProjectFiles.setBaseSize(QtCore.QSize(800, 200))
        self.dockWidget_ProjectFiles.setAutoFillBackground(False)
        self.dockWidget_ProjectFiles.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dockWidget_ProjectFiles.setFloating(False)
        self.dockWidget_ProjectFiles.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_ProjectFiles.setObjectName("dockWidget_ProjectFiles")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton_AddFile = QtGui.QToolButton(self.dockWidgetContents)
        self.toolButton_AddFile.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_AddFile.sizePolicy().hasHeightForWidth())
        self.toolButton_AddFile.setSizePolicy(sizePolicy)
        self.toolButton_AddFile.setMinimumSize(QtCore.QSize(50, 40))
        self.toolButton_AddFile.setMaximumSize(QtCore.QSize(50, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_AddFile.setIcon(icon2)
        self.toolButton_AddFile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_AddFile.setObjectName("toolButton_AddFile")
        self.verticalLayout.addWidget(self.toolButton_AddFile)
        self.toolButton_DelFile = QtGui.QToolButton(self.dockWidgetContents)
        self.toolButton_DelFile.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_DelFile.sizePolicy().hasHeightForWidth())
        self.toolButton_DelFile.setSizePolicy(sizePolicy)
        self.toolButton_DelFile.setMinimumSize(QtCore.QSize(50, 40))
        self.toolButton_DelFile.setMaximumSize(QtCore.QSize(50, 40))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_DelFile.setIcon(icon3)
        self.toolButton_DelFile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_DelFile.setObjectName("toolButton_DelFile")
        self.verticalLayout.addWidget(self.toolButton_DelFile)
        self.line = QtGui.QFrame(self.dockWidgetContents)
        self.line.setMinimumSize(QtCore.QSize(40, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.toolButton_OpenFile = QtGui.QToolButton(self.dockWidgetContents)
        self.toolButton_OpenFile.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_OpenFile.sizePolicy().hasHeightForWidth())
        self.toolButton_OpenFile.setSizePolicy(sizePolicy)
        self.toolButton_OpenFile.setMinimumSize(QtCore.QSize(50, 40))
        self.toolButton_OpenFile.setMaximumSize(QtCore.QSize(50, 40))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_OpenFile.setIcon(icon4)
        self.toolButton_OpenFile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_OpenFile.setObjectName("toolButton_OpenFile")
        self.verticalLayout.addWidget(self.toolButton_OpenFile)
        spacerItem = QtGui.QSpacerItem(20, 189, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.treeWidget = QtGui.QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/mimetypes/doc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setText(0, "Files")
        self.treeWidget.headerItem().setIcon(0, icon5)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Pixmap/ico/16x16/mimetypes/applix.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setText(1, "Regular expression")
        self.treeWidget.headerItem().setIcon(1, icon6)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Pixmap/ico/16x16/filesystems/folder_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon7)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(400)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(400)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.treeWidget.header().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.dockWidget_ProjectFiles.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_ProjectFiles)
        self.action_AddFile = QtGui.QAction(MainWindow)
        self.action_AddFile.setEnabled(False)
        self.action_AddFile.setIcon(icon2)
        self.action_AddFile.setObjectName("action_AddFile")
        self.action_Quit = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon8)
        self.action_Quit.setStatusTip("")
        self.action_Quit.setWhatsThis("")
        self.action_Quit.setObjectName("action_Quit")
        self.action_AboutReqExt = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_AboutReqExt.setIcon(icon9)
        self.action_AboutReqExt.setObjectName("action_AboutReqExt")
        self.action_AboutPlatform = QtGui.QAction(MainWindow)
        self.action_AboutPlatform.setIcon(icon9)
        self.action_AboutPlatform.setObjectName("action_AboutPlatform")
        self.action_Options = QtGui.QAction(MainWindow)
        self.action_Options.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Options.setIcon(icon10)
        self.action_Options.setObjectName("action_Options")
        self.action_ExportRequirementsAsExcelFile = QtGui.QAction(MainWindow)
        self.action_ExportRequirementsAsExcelFile.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/mimetypes/spreadsheet_document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ExportRequirementsAsExcelFile.setIcon(icon11)
        self.action_ExportRequirementsAsExcelFile.setObjectName("action_ExportRequirementsAsExcelFile")
        self.action_OpenProject = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/project_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_OpenProject.setIcon(icon12)
        self.action_OpenProject.setVisible(True)
        self.action_OpenProject.setObjectName("action_OpenProject")
        self.action_SaveProject = QtGui.QAction(MainWindow)
        self.action_SaveProject.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SaveProject.setIcon(icon13)
        self.action_SaveProject.setVisible(True)
        self.action_SaveProject.setObjectName("action_SaveProject")
        self.action_SaveProjectAs = QtGui.QAction(MainWindow)
        self.action_SaveProjectAs.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SaveProjectAs.setIcon(icon14)
        self.action_SaveProjectAs.setObjectName("action_SaveProjectAs")
        self.action_NewProject = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/folder_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_NewProject.setIcon(icon15)
        self.action_NewProject.setObjectName("action_NewProject")
        self.action_ExtractRequirements = QtGui.QAction(MainWindow)
        self.action_ExtractRequirements.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/actions/ico/16x16/actions/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ExtractRequirements.setIcon(icon16)
        self.action_ExtractRequirements.setObjectName("action_ExtractRequirements")
        self.action_CheckForErrors = QtGui.QAction(MainWindow)
        self.action_CheckForErrors.setEnabled(False)
        self.action_CheckForErrors.setIcon(icon16)
        self.action_CheckForErrors.setObjectName("action_CheckForErrors")
        self.action_ExtractFlows = QtGui.QAction(MainWindow)
        self.action_ExtractFlows.setEnabled(False)
        self.action_ExtractFlows.setIcon(icon16)
        self.action_ExtractFlows.setObjectName("action_ExtractFlows")
        self.action_DelFile = QtGui.QAction(MainWindow)
        self.action_DelFile.setEnabled(False)
        self.action_DelFile.setIcon(icon3)
        self.action_DelFile.setObjectName("action_DelFile")
        self.actionExport_2 = QtGui.QAction(MainWindow)
        self.actionExport_2.setObjectName("actionExport_2")
        self.action_OpenFile = QtGui.QAction(MainWindow)
        self.action_OpenFile.setEnabled(False)
        self.action_OpenFile.setIcon(icon4)
        self.action_OpenFile.setObjectName("action_OpenFile")
        self.menuProject.addAction(self.action_AddFile)
        self.menuProject.addAction(self.action_DelFile)
        self.menuProject.addAction(self.action_OpenFile)
        self.menuProject.addSeparator()
        self.menuExport.addAction(self.action_ExportRequirementsAsExcelFile)
        self.menuFile.addAction(self.action_NewProject)
        self.menuFile.addAction(self.action_OpenProject)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_SaveProject)
        self.menuFile.addAction(self.action_SaveProjectAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuProject.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menuHelp.addAction(self.action_AboutPlatform)
        self.menuHelp.addAction(self.action_AboutReqExt)
        self.menuTools.addAction(self.action_ExtractRequirements)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_CheckForErrors)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_Options)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.toolButton_AddFile, self.toolButton_DelFile)
        MainWindow.setTabOrder(self.toolButton_DelFile, self.toolButton_OpenFile)
        MainWindow.setTabOrder(self.toolButton_OpenFile, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.lineEdit_ReqIDFilter)
        MainWindow.setTabOrder(self.lineEdit_ReqIDFilter, self.lineEdit_ReqContentFilter)
        MainWindow.setTabOrder(self.lineEdit_ReqContentFilter, self.tableWidget_Errors)
        MainWindow.setTabOrder(self.tableWidget_Errors, self.tableWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Search for requirements content:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Search for requirements ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Requirement ID", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Requirement Version", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Requirement Content", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabReq), QtGui.QApplication.translate("MainWindow", "Requirements", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_Errors.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Requirement ID", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_Errors.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Error Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabErrors), QtGui.QApplication.translate("MainWindow", "Errors", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProject.setTitle(QtGui.QApplication.translate("MainWindow", "Project Files", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setTitle(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_ProjectFiles.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Project Files", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_AddFile.setText(QtGui.QApplication.translate("MainWindow", "Add file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_DelFile.setText(QtGui.QApplication.translate("MainWindow", "Del file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_OpenFile.setText(QtGui.QApplication.translate("MainWindow", "Open file", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(False)
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.action_AddFile.setText(QtGui.QApplication.translate("MainWindow", "Add requirements file...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AddFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setToolTip(QtGui.QApplication.translate("MainWindow", "Exit application", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutReqExt.setText(QtGui.QApplication.translate("MainWindow", "About Requirements Extractor", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutReqExt.setStatusTip(QtGui.QApplication.translate("MainWindow", "Show Requirements Extractor details", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutPlatform.setText(QtGui.QApplication.translate("MainWindow", "About Platform", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutPlatform.setStatusTip(QtGui.QApplication.translate("MainWindow", "Show details about your platform", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Options.setText(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ExportRequirementsAsExcelFile.setText(QtGui.QApplication.translate("MainWindow", "All requirements in Excel file...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenProject.setText(QtGui.QApplication.translate("MainWindow", "Open project...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveProject.setText(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveProjectAs.setText(QtGui.QApplication.translate("MainWindow", "Save project as...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveProjectAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NewProject.setText(QtGui.QApplication.translate("MainWindow", "New Project...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NewProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ExtractRequirements.setText(QtGui.QApplication.translate("MainWindow", "Extract Requirements", None, QtGui.QApplication.UnicodeUTF8))
        self.action_CheckForErrors.setText(QtGui.QApplication.translate("MainWindow", "Check for errors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ExtractFlows.setText(QtGui.QApplication.translate("MainWindow", "Extract Flows", None, QtGui.QApplication.UnicodeUTF8))
        self.action_DelFile.setText(QtGui.QApplication.translate("MainWindow", "Remove selected file", None, QtGui.QApplication.UnicodeUTF8))
        self.action_DelFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_2.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenFile.setText(QtGui.QApplication.translate("MainWindow", "Open selected file", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))

import qt_resource_file_rc
