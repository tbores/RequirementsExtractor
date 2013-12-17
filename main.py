#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2012, Thomas Bores (http://blog.bores.fr)

import sys
import logging
from PySide.QtGui import QApplication

from MainWindowController import MainWindowController

__version__ = '1.3.2'
__year__ = '2012'

def init_logger():
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # add console handler to the logger
    logger.addHandler(ch)
    
    return logger
    
if __name__ == '__main__':
    logger = init_logger()
    logger.info('ReqExt started')
    
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create a controller object that take care of the UI display and the communication with the data
    mainWindow = MainWindowController(version=__version__, year=__year__, logger=logger)
    # Display program main window
    mainWindow.show()
    # Run the run Qt loop
    sys.exit(app.exec_())
    logger.info('ReqExt finished')