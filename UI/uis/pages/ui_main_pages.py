# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\研究生\研一\空间分析软件\代码\UI测试\UI\uis\pages\main_pages.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        MainPages.setObjectName("MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QtWidgets.QVBoxLayout(MainPages)
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName("main_pages_layout")
        self.pages = QtWidgets.QStackedWidget(MainPages)
        self.pages.setObjectName("pages")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet("font-size: 14pt")
        self.page_1.setObjectName("page_1")
        self.page_1_layout = QtWidgets.QVBoxLayout(self.page_1)
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName("page_1_layout")
        self.frame = QtWidgets.QFrame(self.page_1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.page_1_layout.addWidget(self.frame)
        self.pages.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("QFrame {\n"
"    font-size: 16pt;\n"
"}")
        self.page_2.setObjectName("page_2")
        self.page_2_layout = QtWidgets.QVBoxLayout(self.page_2)
        self.page_2_layout.setObjectName("page_2_layout")
        self.empty_page_label = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.empty_page_label.setObjectName("empty_page_label")
        self.page_2_layout.addWidget(self.empty_page_label)
        self.pages.addWidget(self.page_2)
        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)
        self.pages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainPages)

    def retranslateUi(self, MainPages):
        _translate = QtCore.QCoreApplication.translate
        MainPages.setWindowTitle(_translate("MainPages", "Form"))
        self.empty_page_label.setText(_translate("MainPages", "Empty Page"))
