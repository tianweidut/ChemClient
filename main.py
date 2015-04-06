#coding: utf-8

import sys
from PyQt4.QtCore import QUrl
from PyQt4 import QtCore, QtGui

from ui import SimpleChemUI

from conf import (HISTORY_URL,
                  CALCULATE_URL, USERINFO_URL, LOGOUT_URL)


class WebBrowser2(QtGui.QWidget):
    def __init__(self, parent=None):
        super(WebBrowser2, self).__init__(parent)
        self.ui = SimpleChemUI()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.calculate_btn, QtCore.SIGNAL("clicked()"), self.calculate)
        QtCore.QObject.connect(self.ui.history_btn, QtCore.SIGNAL("clicked()"), self.history)
        QtCore.QObject.connect(self.ui.logout_btn, QtCore.SIGNAL("clicked()"), self.logout)
        QtCore.QObject.connect(self.ui.userinfo_btn, QtCore.SIGNAL("clicked()"), self.userinfo)

        QtCore.QMetaObject.connectSlotsByName(self)

    def history(self):
        self.ui.webView.setUrl(QUrl(HISTORY_URL))

    def calculate(self):
        self.ui.webView.setUrl(QUrl(CALCULATE_URL))

    def userinfo(self):
        self.ui.webView.setUrl(QUrl(USERINFO_URL))

    def logout(self):
        self.ui.webView.setUrl(QUrl(LOGOUT_URL))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = WebBrowser2()
    myapp.show()
    sys.exit(app.exec_())
