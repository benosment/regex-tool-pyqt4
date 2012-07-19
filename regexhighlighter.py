#! /usr/bin/env python
#
# Ben Osment
# Tue Jul 17 07:00:00 2012

from PyQt4.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont
from PyQt4.QtCore import Qt, QRegExp


class RegexHighlighter(QSyntaxHighlighter):
    def __init__(self, widget):
        QSyntaxHighlighter.__init__(self, widget)
        self.regex = None
        # create format type
        self.odd_format = QTextCharFormat()
        self.odd_format.setFontWeight(QFont.Bold)
        self.odd_format.setForeground(Qt.darkBlue)
        self.even_format = QTextCharFormat()
        self.even_format.setFontWeight(QFont.Bold)
        self.even_format.setForeground(Qt.darkMagenta)

    def set_regex(self, exp):
        self.regex = QRegExp(exp)

    def highlightBlock(self, text):
        if not self.regex:
            return
        matches = 0
        pos = self.regex.indexIn(text, 0)
        while (pos >= 0):
            length = self.regex.matchedLength()
            matches += 1
            if matches % 2 == 0:
                self.setFormat(pos, length, self.even_format)
            else:
                self.setFormat(pos, length, self.odd_format)
            # handle wildcard (*)
            if length == 0:
                pos += 1
            pos = self.regex.indexIn(text, pos + length)
