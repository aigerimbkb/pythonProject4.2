#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()  # получаем наш текст
        txt=text.split()
        reserved_array = ["abs", "absolute", "and", "arctan", "array", "as", "asm", "begin", "boolean", "break",
        "case", "char", "class", "const", "constructor", "continue", "cos", "destructor", "dispose", "div",
        "do", "downto", "else", "end", "eof", "eoln", "except", "exp", "exports", "false", "file", "finalization",
        "finally", "for", "function", "goto",	"if", "implementation",	"in", "inherited", "initialization", "inline",
        "input", "integer", "interface", "is", "label", "library", "ln", "int", "mod", "new", "nil", "not", "object",
        "odd", "of", "on", "operator", "or", "ord", "output", "pack", "packed", "page", "pred", "procedure", "program",
        "property", "raise", "read", "readln", "real", "record", "reintroduce", "repeat", "reset", "rewrite", "round",
        "self", "set", "shl", "shr", "sin", "sqr", "sqrt", "string", "succ", "text", "then", "threadvar", "to", "true",
        "trunc", "try", "type", "unit", "until", "uses", "var", "while", "with", "write", "writeln", "xor"]

        for s in txt:
            for word in reserved_array:
                if s==word:
                    s=s.upper()
            self.textEdit_words.insertPlainText(s + "\n")



    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
