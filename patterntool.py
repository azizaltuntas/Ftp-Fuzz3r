# -*- coding: utf-8 -*-

#
#
#Coded - AbdulAziz Altuntaş - @eScCopyright
#
#

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal, pyqtSlot
import codecs , binascii
import struct

class colors(object):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

import sys
from string import digits, ascii_lowercase, ascii_uppercase


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):


    def offset(self):

        if "0x" in self.eipvalue.text() and len(self.eipvalue.text()) == 10:


            self.new = self.eipvalue.text()[2:]
            #self.little = struct.pack("<H", '%s' %self.eipvalue.text())

            self.little2 = binascii.a2b_hex('%s' %self.new)

            self.c = ''
            self.c += self.little2[::-1]

            self._ = ''
            self.lengt = 20281

            for self.upper in ascii_uppercase:
                for self.lower in ascii_lowercase:
                    for self.digit in digits:
                        if isinstance(Ui_MainWindow, object) and len(self._) < self.lengt:
                            self._ += (self.upper + self.lower + self.digit)

            if self.c in self._:

                self.say = self._.find(self.c)
                self.offsetwid.setText("After [+]"+"<font color='black'><b>"+str(self.say)+"</b>"+" Character [+4Byte EIP]")

            else:

                self.message("No Crash Length", "Fauly Format", SyntaxWarning)


        else:
            self.message("Fauly Format","Eip Format : 0x78655363\n[Char Length 10 !]",SyntaxError)


    def message(self,text,inf,title):
        self.msg = QtGui.QMessageBox()
        self.msg.setText('%s' %text)
        self.msg.setInformativeText('%s' %inf) #0x37694136
        self.msg.setWindowTitle('%s' %title)

        self.execmsg = self.msg.exec_()

    def create(self):

        self._ = ''
        self.lengt = 20281 # Maximum Lengt : python s.py > patternlen.txt / cat patternlen.txt | wc -c RETURN : 20281

        for self.upper in ascii_uppercase:
            for self.lower in ascii_lowercase:
                for self.digit in digits:
                    if isinstance(Ui_MainWindow, object) and len(self._) < self.lengt:
                        self._ += (self.upper + self.lower + self.digit)

        self.final = self._[:self.patternlen.value()]
                        
        self.patternwid.setText(self.final)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 261, 231))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 50, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.patternlen = QtGui.QSpinBox(self.groupBox)
        self.patternlen.setGeometry(QtCore.QRect(90, 50, 61, 21))
        self.patternlen.setMinimum(1)
        self.patternlen.setMaximum(20281)
        self.patternlen.setObjectName(_fromUtf8("patternlen"))
        self.patternwid = QtGui.QTextEdit(self.groupBox)
        self.patternwid.setReadOnly(True)
        self.patternwid.setGeometry(QtCore.QRect(10, 90, 231, 81))
        self.patternwid.setObjectName(_fromUtf8("patternwid"))
        self.patterncopy = QtGui.QPushButton(self.groupBox)
        self.patterncopy.setGeometry(QtCore.QRect(70, 190, 85, 27))
        self.patterncopy.setInputMethodHints(QtCore.Qt.ImhNone)
        self.patterncopy.setObjectName(_fromUtf8("patterncopy"))
        self.getpattern = QtGui.QPushButton(self.groupBox)
        self.getpattern.setGeometry(QtCore.QRect(160, 50, 81, 21))
        self.getpattern.setObjectName(_fromUtf8("getpattern"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 60, 271, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 61, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.eipvalue = QtGui.QLineEdit(self.groupBox_2)
        self.eipvalue.setGeometry(QtCore.QRect(70, 50, 91, 21))
        self.eipvalue.setMaxLength(10)
        self.eipvalue.setObjectName(_fromUtf8("eipvalue"))
        self.getoffset = QtGui.QPushButton(self.groupBox_2)
        self.getoffset.setGeometry(QtCore.QRect(170, 50, 91, 21))
        self.getoffset.setObjectName(_fromUtf8("getoffset"))
        self.offsetwid = QtGui.QTextEdit(self.groupBox_2)
        self.offsetwid.setReadOnly(True)
        self.offsetwid.setGeometry(QtCore.QRect(0, 90, 256, 21))
        self.offsetwid.setObjectName(_fromUtf8("offsetwid"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 56, 17))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 231, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.getpattern.clicked.connect(self.create)
        self.getoffset.clicked.connect(self.offset)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.patterncopy, QtCore.SIGNAL(_fromUtf8("clicked()")), self.patternwid.selectAll)
        QtCore.QObject.connect(self.patterncopy, QtCore.SIGNAL(_fromUtf8("clicked()")), self.patternwid.copy)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pattern Tool", None))
        self.groupBox.setTitle(_translate("MainWindow", "Pattern Create", None))
        self.label.setText(_translate("MainWindow", "Pattern Lengt :", None))
        self.patterncopy.setText(_translate("MainWindow", "Copy", None))
        self.getpattern.setText(_translate("MainWindow", "Get Pattern", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Pattern Offset", None))
        self.label_2.setText(_translate("MainWindow", "EIP Value :", None))
        self.getoffset.setText(_translate("MainWindow", "Get Offset", None))
        self.label_4.setText(_translate("MainWindow", "Pattern Creater - Offset Calculation Tool", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle('gtk+')
    win = Ui_MainWindow()
    cls = QtGui.QMainWindow()
    win.setupUi(cls)
    cls.show()
    sys.exit(app.exec_())
