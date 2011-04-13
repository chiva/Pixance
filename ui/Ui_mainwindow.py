# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Universidad\Dropbox\Trabajos\Programas\Pixance\ui\mainwindow.ui'
#
# Created: Wed Apr 13 18:31:41 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(252, 84)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.leApiKey = QtGui.QLineEdit(self.centralWidget)
        self.leApiKey.setGeometry(QtCore.QRect(70, 20, 171, 20))
        self.leApiKey.setObjectName(_fromUtf8("leApiKey"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btStart = QtGui.QPushButton(self.centralWidget)
        self.btStart.setGeometry(QtCore.QRect(80, 50, 75, 23))
        self.btStart.setObjectName(_fromUtf8("btStart"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pixance v0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "API Key", None, QtGui.QApplication.UnicodeUTF8))
        self.btStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

