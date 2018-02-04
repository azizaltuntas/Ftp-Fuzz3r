# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys ,os
import  multiprocessing
import subprocess
import socket
import time


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

class colors(object):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


class Ui_MainWindow(object):



    def patterncall(self):


        self.man = ''

        for _ in os.listdir(os.getcwd()):
            self.man += _

        if "patterntool" in self.man:


            self.call = subprocess.Popen(["python", "patterntool.py"], shell=False) # WARNING ! VULNERABLE FUNCTION..

        else:

            self.message("Pattern Tool Not Found!","Please curl patterntool", Warning)


    def message(self,text,inf,title):
         self.msg = QtGui.QMessageBox()
         self.msg.setText('%s' %text)
         self.msg.setInformativeText('%s' %inf)
         self.msg.setWindowTitle('%s' %title)

         self.execmsg = self.msg.exec_()

    def help(self):

        self.msg = QtGui.QMessageBox()
        self.msg.setText("<font color='white'><p><b>Coded : Abdulaziz Altuntas - Gh:@azizaltuntas</b></p>")
        self.msg.setInformativeText(" "*30+"Tool Information\n"
                                    "Host : Host Ip\n"
                                    "Port : Host Port\n"
                                    "CMD  : Fuzz Ftp Command\n"
                                    "Cursor : Processor Cursor\n"
                                    "StartSize : Starting Pattern Length[Example: 100]\n"
                                    "StepSize  : StartSize += StepSize\n"
                                    "EndSize   : Finish Pattern Length\n"
                                    "TimeOut   : TimeOut :)\n"
                                    "Pattern Tool : Open Pattern Tool\n"
                                    "Custom Pattern : Send Created Pattern[Pattern Tool]")
        self.msg.setWindowTitle("About")

        self.execmsg = self.msg.exec_()


    def addmode(self):

        if not self.host.text():
            self.message("Free Space ! ", "Please Enter Host", Warning)
        elif not self.port.text():
            self.message("Free Space ! ", "Please Enter Port", Warning)
        elif not  self.command.text():
            self.message("Free Space ! ", "Please Enter CMD", Warning)


        else:

            self.message("Please Wait..Process ", "Click to Start !", Warning)
            self.control()


    def control(self):


        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout.value())
            s.connect((self.host.text(), int(self.port.text())))
            s.recv(1024)
            if not self.custompattern.text():

                self.fuzz()
            else:

                self.startsize.setMaximum(0)
                self.stepsize.setMaximum(0)
                self.endsize.setMaximum(0)
                self.oneshot()
                pass

        except socket.error:
            self.message(Warning,"Connection Fail !", "Connect Info")



    def message(self,text,inf,title):
        self.msg = QtGui.QMessageBox()
        self.msg.setText('%s' %text)
        self.msg.setInformativeText('%s' %inf) #0x37694136
        self.msg.setWindowTitle('%s' %title)

        self.execmsg = self.msg.exec_()

    def oneshot(self):
        try:

            self.startsize.setRange(0, 500)
            self.endsize.setRange(0, 5000)
            self.stepsize.setRange(50,300)

            self.one = ''
            self.one += self.custompattern.text()


            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout.value())
            s.connect((self.host.text(), int(self.port.text())))
            s.recv(1024)
            s.send('USER anonymous\r\n')
            s.recv(1024)
            s.send('PASS anonymous\r\n')
            s.recv(1024)
            s.send('%s' %self.command.text() + '%s' %self.one + "\r\n")
            s.close()

            self.cursor.addItem("[+]Pattern Successful ! - Length: "+'%s' %str(len(self.custompattern.text())) + " Byte Sent..")
            self.custompattern.clear()

        except:
            self.cursor.addItem("One Shot Failed !")

    def fuzz(self):

        self.startbabe = self.startsize.value()
        self.endbabe = self.endsize.value()
        self.stepbabe = self.stepsize.value()

        self.buffpattern = '\x41' * self.startbabe
        self.songoku   = 0


        while self.endbabe > self.songoku:

            try:

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self.timeout.value())
                s.connect((self.host.text(), int(self.port.text())))
                s.recv(1024)

                self.songoku += self.stepbabe
                s.send('%s' %self.command.text() + self.buffpattern + "\r\n")
                s.close()

                self.cursor.addItem("Send Pattern Lengt[No Crash]: " + str(len(self.buffpattern)))

                self.buffpattern += '\x41' * self.stepbabe

            except:
                self.cursor.addItem("[+]Send Pattern Lengt[Crash !]: " + str(len(self.buffpattern)))
                self.message("Finish","Crash Seccussful !", Warning)
                break


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(True)
        self.Int = QtGui.QDoubleValidator()
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(560, 50, 181, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 61, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 110, 56, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 56, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.startsize = QtGui.QSpinBox(self.groupBox)
        self.startsize.setGeometry(QtCore.QRect(90, 50, 51, 20))
        self.startsize.setObjectName(_fromUtf8("startsize"))
        self.startsize.setRange(0,500)
        self.endsize = QtGui.QSpinBox(self.groupBox)
        self.endsize.setRange(0,5000)
        self.endsize.setGeometry(QtCore.QRect(90, 80, 51, 20))
        self.endsize.setObjectName(_fromUtf8("endsize"))
        self.stepsize = QtGui.QSpinBox(self.groupBox)
        self.stepsize.setGeometry(QtCore.QRect(90, 110, 51, 20))
        self.stepsize.setObjectName(_fromUtf8("stepsize"))
        self.stepsize.setRange(50,300)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 56, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.timeout = QtGui.QSpinBox(self.groupBox)
        self.timeout.setGeometry(QtCore.QRect(90, 140, 51, 21))
        self.timeout.setObjectName(_fromUtf8("timeout"))
        self.timeout.setRange(1,10)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 50, 221, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 56, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 50, 56, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.host = QtGui.QLineEdit(self.groupBox_2)
        self.host.setGeometry(QtCore.QRect(50, 50, 113, 21))
        self.host.setAutoFillBackground(False)
        self.host.setText(_fromUtf8(""))
        self.host.setMaxLength(15)
        self.host.setCursorPosition(0)
        self.host.setReadOnly(False)
        self.host.setPlaceholderText(_fromUtf8(""))
        self.host.setObjectName(_fromUtf8("host"))
        self.host.setValidator(self.Int)
        self.inf = QtGui.QLabel(MainWindow)
        self.inf.setGeometry(QtCore.QRect(330,120,150,27))
        self.inf.setObjectName(_fromUtf8("inf"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 56, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.port = QtGui.QLineEdit(self.groupBox_2)
        self.port.setGeometry(QtCore.QRect(50, 80, 113, 21))
        self.port.setMaxLength(5)
        self.port.setPlaceholderText(_fromUtf8(""))
        self.port.setObjectName(_fromUtf8("port"))
        self.port.setValidator(self.Int)
        self.command = QtGui.QLineEdit(self.groupBox_2)
        self.command.setGeometry(QtCore.QRect(50, 110, 113, 21))
        self.command.setMaxLength(8)
        self.command.setPlaceholderText(_fromUtf8(""))
        self.command.setObjectName(_fromUtf8("command"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 350, 491, 181))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.cursor = QtGui.QListWidget(self.groupBox_3)
        self.cursor.setGeometry(QtCore.QRect(20, 20, 421, 130))
        self.cursor.setObjectName(_fromUtf8("cursor"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(169, 230, 431, 111))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.custompattern = QtGui.QLineEdit(self.groupBox_4)
        self.custompattern.setGeometry(QtCore.QRect(10, 20, 421, 70))
        self.custompattern.setObjectName(_fromUtf8("custompattern"))

        self.getpattern = QtGui.QPushButton(self.centralwidget)
        self.getpattern.setGeometry(QtCore.QRect(440, 190, 85, 27))
        self.getpattern.setObjectName(_fromUtf8("pushButton"))
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(260, 190, 85, 27))
        self.start.setObjectName(_fromUtf8("start"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.start.clicked.connect(self.addmode)


        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("activated()")), self.help)
        QtCore.QObject.connect(self.getpattern, QtCore.SIGNAL(_fromUtf8("clicked()")), self.patterncall)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ftp Fuzz3r", None))
        self.groupBox.setTitle(_translate("MainWindow", "Options", None))
        self.label_7.setText(_translate("MainWindow", "EndSize   :", None))
        self.label_8.setText(_translate("MainWindow", "StepSize  :", None))
        self.label_6.setText(_translate("MainWindow", "StartSize :", None))
        self.label_5.setText(_translate("MainWindow", "Timeout  :", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Settings", None))
        self.label_2.setText(_translate("MainWindow", "Port  :", None))
        self.label.setText(_translate("MainWindow", "Host :", None))
        self.label_3.setText(_translate("MainWindow", "CMD :", None))
        self.inf.setText(_translate("MainWindow", "Github: @azizaltuntas", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "   Cursor", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Custom Pattern (One Shot)", None))
        self.getpattern.setText(_translate("MainWindow", "Pattern Tool", None))
        self.start.setText(_translate("MainWindow", "Start", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle('gtk+')
    win = Ui_MainWindow()
    cls = QtGui.QMainWindow()
    win.setupUi(cls)
    cls.show()
    sys.exit(app.exec_())
