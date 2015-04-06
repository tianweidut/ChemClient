#coding: utf-8

import sys
from PyQt4.QtCore import QUrl, SIGNAL, QByteArray, QString
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView, QWebPage
from PyQt4 import QtCore, QtGui

from ui import SimpleChemUI

from conf import (HOMEPAGE_URL, HISTORY_URL,
                  CALCULATE_URL, USERINFO_URL, LOGOUT_URL)


class WebPage(QWebPage):
    def __init__(self):
        QWebPage.__init__(self)
        self.user_agent = "Mozilla/5.0 Chrome/38.0.2125.122 Safari/537.36 ChemClient"

    def userAgentForUrl(self, url):
        return self.user_agent
        return QString(QByteArray(self.user_agent))


class WebBrowser(QApplication):
    def __init__(self, url=None):
        super(WebBrowser, self).__init__(sys.argv)
        self.url = url or HOMEPAGE_URL
        self.web_view = QWebView()
        self.web_page = WebPage()
        self.web_view.setPage(self.web_page)
        self.web_frame = self.web_page.currentFrame()
        self.connect(self.web_view, SIGNAL('loadFinished(bool)'), self.load_finished)
        self.web_frame.load(QUrl(self.url))
        self.web_view.show()

    def load_finished(self, is_finished):
        if is_finished:
            print self.web_page.mainFrame().contentsSize()
            #self.web_page.setViewportSize(self.web_page.mainFrame().contentsSize())
            print self.web_page.currentFrame().url().toString()
        else:
            print 'wait....'


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
