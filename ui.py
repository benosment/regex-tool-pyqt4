#! /usr/bin/env python
#
# Ben Osment
# Sun Jul 15 08:41:39 2012

import sys
from PyQt4 import QtGui, QtCore

class UI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(800, 600)
        self.setWindowTitle('Regex Tool')
        self.center()

        aboutAction = QtGui.QAction('&About', self)
        aboutAction.setStatusTip('Display information about regex tool')

        helpAction = QtGui.QAction('&Help', self)
        helpAction.setShortcut('Ctrl+H')
        helpAction.setStatusTip('Display help')

        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(aboutAction)
        fileMenu.addAction(helpAction)
        fileMenu.addAction(exitAction)

        # add main elements
        self.grid = Grid(self)
        self.grid.setGeometry(QtCore.QRect(0,0,800,500))
        self.setCentralWidget(self.grid)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

# TODO split to a new file? 
class Grid(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('<b>Text</b>'), 1, 0)
        self.textbox = QtGui.QTextEdit(self)
        grid.addWidget(self.textbox, 2, 0, 2, 0)
        grid.addWidget(QtGui.QLabel('<b>Regular Expression</b>'), 6, 0)
        self.regex_box = QtGui.QTextEdit(self)
        grid.addWidget(self.regex_box, 7, 0, 2, 0)
        self.setLayout(grid)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
