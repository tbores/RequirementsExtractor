pyside-uic -o MainWindowView.py MainWindow.ui
pyside-uic -o Dialog_AddFileView.py Dialog_AddFile.ui
pyside-uic -o Dialog_NewProjectView.py Dialog_NewProject.ui 
pyside-uic -o Dialog_OptionsView.py Dialog_Options.ui
pyside-rcc -o qt_resource_file_rc.py qt_resource_file.qrc
pause