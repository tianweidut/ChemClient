# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Nov 25 22:55:39 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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


class SimpleChemUI(object):

    def setupUi(self, Chem):
        Chem.setObjectName(_fromUtf8("Chem"))
        Chem.resize(1124, 800)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Chem.sizePolicy().hasHeightForWidth())
        Chem.setSizePolicy(sizePolicy)
        Chem.setMinimumSize(QtCore.QSize(1124, 800))
        Chem.setMaximumSize(QtCore.QSize(1124, 800))
        Chem.setBaseSize(QtCore.QSize(0, 0))

        self.verticalLayout = QtGui.QVBoxLayout(Chem)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.webView = QtWebKit.QWebView(Chem)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(
            self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setAutoFillBackground(False)
        self.webView.setUrl(
            QtCore.QUrl(
                _fromUtf8("http://202.118.73.59/accounts/login/")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalFrame = QtGui.QFrame(Chem)
        self.horizontalFrame.setObjectName(_fromUtf8("horizontalFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.userinfo_btn = QtGui.QToolButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.userinfo_btn.setFont(font)
        self.userinfo_btn.setObjectName(_fromUtf8("userinfo_btn"))
        self.horizontalLayout_2.addWidget(self.userinfo_btn)
        self.calculate_btn = QtGui.QToolButton(self.horizontalFrame)
        self.calculate_btn.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_btn.setFont(font)
        self.calculate_btn.setIconSize(QtCore.QSize(40, 40))
        self.calculate_btn.setObjectName(_fromUtf8("calculate_btn"))
        self.horizontalLayout_2.addWidget(self.calculate_btn)
        self.history_btn = QtGui.QToolButton(self.horizontalFrame)
        self.logout_btn = QtGui.QToolButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.history_btn.setFont(font)
        self.logout_btn.setFont(font)
        self.history_btn.setObjectName(_fromUtf8("history_btn"))
        self.logout_btn.setObjectName(_fromUtf8("logout_btn"))
        self.horizontalLayout_2.addWidget(self.history_btn)
        self.horizontalLayout_2.addWidget(self.logout_btn)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(Chem)
        QtCore.QMetaObject.connectSlotsByName(Chem)

    def retranslateUi(self, Chem):
        Chem.setWindowTitle(_translate("Chem", "Chem", None))
        self.userinfo_btn.setText(_translate("Chem", "用户信息", None))
        self.calculate_btn.setText(_translate("Chem", "模型计算", None))
        self.history_btn.setText(_translate("Chem", "计算历史", None))
        self.logout_btn.setText(_translate("Chem", "登出", None))


from PyQt4 import QtWebKit
