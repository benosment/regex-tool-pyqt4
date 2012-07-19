#! /usr/bin/env python
#
# Ben Osment
# Sun Jul 15 08:41:39 2012

import sys
from PyQt4 import QtGui, QtCore
from regexhighlighter import RegexHighlighter


class UI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(600, 400)
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
        self.box = Box(self)
        self.box.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.setCentralWidget(self.box)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


class Box(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        box = QtGui.QVBoxLayout()
        box.addWidget(QtGui.QLabel('<b>Text</b>'))
        self.textbox = QtGui.QTextEdit(self)
        box.addWidget(self.textbox)
        box.addWidget(QtGui.QLabel('<b>Regular Expression</b>'))
        self.regex_box = QtGui.QTextEdit(self)
        self.regex_box.textChanged.connect(self.textChanged)
        box.addWidget(self.regex_box)
        self.setLayout(box)
        self.highlighter = RegexHighlighter(self.textbox.document())

    def textChanged(self):
        regex_val = "%s" % self.regex_box.document().toPlainText()
        self.highlighter.set_regex(regex_val)
        self.highlighter.rehighlight()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
