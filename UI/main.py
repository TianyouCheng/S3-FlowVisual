# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\研究生\研一\空间分析软件\代码\核心功能实验\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 590)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/qgis.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 291, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget.setMinimumSize(QtCore.QSize(150, 0))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 120, 111, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 230, 111, 91))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_10.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(510, 30, 131, 361))
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 111, 91))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 120, 111, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 230, 111, 91))
        self.pushButton_6.setAutoFillBackground(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.listWidget.setMaximumSize(QtCore.QSize(40, 16777215))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget.setObjectName("tabWidget")
        self.rasterLayerInfoTab = QtWidgets.QWidget()
        self.rasterLayerInfoTab.setObjectName("rasterLayerInfoTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.rasterLayerInfoTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.rasterLayerInfoTab)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.rasterLayerInfoTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.label_3 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_1.addWidget(self.label_3)
        self.rasterNameLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterNameLabel.setObjectName("rasterNameLabel")
        self.horizontalLayout_1.addWidget(self.rasterNameLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.rasterSourceLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterSourceLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.rasterSourceLabel.setObjectName("rasterSourceLabel")
        self.horizontalLayout_2.addWidget(self.rasterSourceLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.rasterMemoryLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterMemoryLabel.setObjectName("rasterMemoryLabel")
        self.horizontalLayout_3.addWidget(self.rasterMemoryLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.label_9 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.line_3 = QtWidgets.QFrame(self.rasterLayerInfoTab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.rasterExtentLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterExtentLabel.setObjectName("rasterExtentLabel")
        self.horizontalLayout_4.addWidget(self.rasterExtentLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.rasterWidthLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterWidthLabel.setObjectName("rasterWidthLabel")
        self.horizontalLayout_5.addWidget(self.rasterWidthLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.rasterHeightLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterHeightLabel.setObjectName("rasterHeightLabel")
        self.horizontalLayout_6.addWidget(self.rasterHeightLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_16.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.rasterDataTypeLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterDataTypeLabel.setObjectName("rasterDataTypeLabel")
        self.horizontalLayout_7.addWidget(self.rasterDataTypeLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_18.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        self.rasterBandNumLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterBandNumLabel.setObjectName("rasterBandNumLabel")
        self.horizontalLayout_8.addWidget(self.rasterBandNumLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_20 = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.label_20.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.rasterCrsLabel = QtWidgets.QLabel(self.rasterLayerInfoTab)
        self.rasterCrsLabel.setObjectName("rasterCrsLabel")
        self.horizontalLayout_9.addWidget(self.rasterCrsLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.rasterLayerInfoTab, "")
        self.vectorLayerInfoTab = QtWidgets.QWidget()
        self.vectorLayerInfoTab.setObjectName("vectorLayerInfoTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.vectorLayerInfoTab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_26 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_9.addWidget(self.label_26)
        self.line_6 = QtWidgets.QFrame(self.vectorLayerInfoTab)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_9.addWidget(self.line_6)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_25 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_25.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_21.addWidget(self.label_25)
        self.vectorNameLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorNameLabel.setObjectName("vectorNameLabel")
        self.horizontalLayout_21.addWidget(self.vectorNameLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_32 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_32.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_27.addWidget(self.label_32)
        self.vectorSourceLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorSourceLabel.setObjectName("vectorSourceLabel")
        self.horizontalLayout_27.addWidget(self.vectorSourceLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_30 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_30.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_25.addWidget(self.label_30)
        self.vectorMemoryLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorMemoryLabel.setObjectName("vectorMemoryLabel")
        self.horizontalLayout_25.addWidget(self.vectorMemoryLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_25)
        self.label_34 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_9.addWidget(self.label_34)
        self.line_5 = QtWidgets.QFrame(self.vectorLayerInfoTab)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_9.addWidget(self.line_5)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_27 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_27.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_22.addWidget(self.label_27)
        self.vectorExtentLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorExtentLabel.setObjectName("vectorExtentLabel")
        self.horizontalLayout_22.addWidget(self.vectorExtentLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_33 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_33.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_28.addWidget(self.label_33)
        self.vectorGeoTypeLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorGeoTypeLabel.setObjectName("vectorGeoTypeLabel")
        self.horizontalLayout_28.addWidget(self.vectorGeoTypeLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_31 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_31.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_26.addWidget(self.label_31)
        self.vectorFeatureNumLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorFeatureNumLabel.setObjectName("vectorFeatureNumLabel")
        self.horizontalLayout_26.addWidget(self.vectorFeatureNumLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_35 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_35.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_29.addWidget(self.label_35)
        self.vectorEncodingLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorEncodingLabel.setObjectName("vectorEncodingLabel")
        self.horizontalLayout_29.addWidget(self.vectorEncodingLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_28 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_28.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_23.addWidget(self.label_28)
        self.vectorCrsLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorCrsLabel.setObjectName("vectorCrsLabel")
        self.horizontalLayout_23.addWidget(self.vectorCrsLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_29 = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.label_29.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_24.addWidget(self.label_29)
        self.vectorDpLabel = QtWidgets.QLabel(self.vectorLayerInfoTab)
        self.vectorDpLabel.setObjectName("vectorDpLabel")
        self.horizontalLayout_24.addWidget(self.vectorDpLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_24)
        self.tabWidget.addTab(self.vectorLayerInfoTab, "")
        self.rasterLayerRenderTab = QtWidgets.QWidget()
        self.rasterLayerRenderTab.setObjectName("rasterLayerRenderTab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.rasterLayerRenderTab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.rasterLayerRenderTab)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.line_4 = QtWidgets.QFrame(self.rasterLayerRenderTab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_10.addWidget(self.line_4)
        self.layerRenderLayout = QtWidgets.QVBoxLayout()
        self.layerRenderLayout.setObjectName("layerRenderLayout")
        self.verticalLayout_10.addLayout(self.layerRenderLayout)
        self.pushButton_rasterApply = QtWidgets.QPushButton(self.rasterLayerRenderTab)
        self.pushButton_rasterApply.setStyleSheet("")
        self.pushButton_rasterApply.setObjectName("pushButton_rasterApply")
        self.verticalLayout_10.addWidget(self.pushButton_rasterApply)
        self.tabWidget.addTab(self.rasterLayerRenderTab, "")
        self.vectorLayerRenderTab = QtWidgets.QWidget()
        self.vectorLayerRenderTab.setObjectName("vectorLayerRenderTab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.vectorLayerRenderTab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_36 = QtWidgets.QLabel(self.vectorLayerRenderTab)
        self.label_36.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_11.addWidget(self.label_36)
        self.line_7 = QtWidgets.QFrame(self.vectorLayerRenderTab)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_11.addWidget(self.line_7)
        self.layerRenderLayout_2 = QtWidgets.QVBoxLayout()
        self.layerRenderLayout_2.setObjectName("layerRenderLayout_2")
        self.vecterRenderCB = QtWidgets.QComboBox(self.vectorLayerRenderTab)
        self.vecterRenderCB.setObjectName("vecterRenderCB")
        self.vecterRenderCB.addItem("")
        self.vecterRenderCB.addItem("")
        self.vecterRenderCB.addItem("")
        self.layerRenderLayout_2.addWidget(self.vecterRenderCB)
        self.comboTabWidget = QtWidgets.QTabWidget(self.vectorLayerRenderTab)
        self.comboTabWidget.setObjectName("comboTabWidget")
        self.singleRender = QtWidgets.QWidget()
        self.singleRender.setObjectName("singleRender")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.singleRender)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.singleRenderLayout = QtWidgets.QVBoxLayout()
        self.singleRenderLayout.setObjectName("singleRenderLayout")
        self.verticalLayout_12.addLayout(self.singleRenderLayout)
        self.comboTabWidget.addTab(self.singleRender, "")
        self.categoryRender = QtWidgets.QWidget()
        self.categoryRender.setObjectName("categoryRender")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.categoryRender)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.cateRenderLayout = QtWidgets.QVBoxLayout()
        self.cateRenderLayout.setObjectName("cateRenderLayout")
        self.verticalLayout_13.addLayout(self.cateRenderLayout)
        self.comboTabWidget.addTab(self.categoryRender, "")
        self.graduatedRender = QtWidgets.QWidget()
        self.graduatedRender.setObjectName("graduatedRender")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.graduatedRender)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gradRenderLayout = QtWidgets.QVBoxLayout()
        self.gradRenderLayout.setObjectName("gradRenderLayout")
        self.verticalLayout_3.addLayout(self.gradRenderLayout)
        self.comboTabWidget.addTab(self.graduatedRender, "")
        self.layerRenderLayout_2.addWidget(self.comboTabWidget)
        self.verticalLayout_11.addLayout(self.layerRenderLayout_2)
        self.pushButton_vectorApply = QtWidgets.QPushButton(self.vectorLayerRenderTab)
        self.pushButton_vectorApply.setObjectName("pushButton_vectorApply")
        self.verticalLayout_11.addWidget(self.pushButton_vectorApply)
        self.tabWidget.addTab(self.vectorLayerRenderTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.actionOpenShp = QtWidgets.QAction(MainWindow)
        self.actionOpenShp.setObjectName("actionOpenShp")
        self.actionOpenRaster = QtWidgets.QAction(MainWindow)
        self.actionOpenRaster.setObjectName("actionOpenRaster")
        self.actiontest1 = QtWidgets.QAction(MainWindow)
        self.actiontest1.setObjectName("actiontest1")
        self.actiontest2 = QtWidgets.QAction(MainWindow)
        self.actiontest2.setObjectName("actiontest2")
        self.actiontest3 = QtWidgets.QAction(MainWindow)
        self.actiontest3.setObjectName("actiontest3")
        self.menuOpen.addAction(self.actionOpenShp)
        self.menuOpen.addAction(self.actionOpenRaster)
        self.menu.addAction(self.actiontest1)
        self.menu.addAction(self.actiontest2)
        self.menu.addAction(self.actiontest3)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.comboTabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.menuOpen.setTitle(_translate("MainWindow", "打开"))
        self.menu.setTitle(_translate("MainWindow", "测试"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "信息"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "渲染"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "常规信息"))
        self.label_3.setText(_translate("MainWindow", "名称"))
        self.rasterNameLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "路径"))
        self.rasterSourceLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "大小合计"))
        self.rasterMemoryLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "栅格信息"))
        self.label_10.setText(_translate("MainWindow", "范围"))
        self.rasterExtentLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "宽度"))
        self.rasterWidthLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "高度"))
        self.rasterHeightLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "数据类型"))
        self.rasterDataTypeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "波段数量"))
        self.rasterBandNumLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "坐标系"))
        self.rasterCrsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rasterLayerInfoTab), _translate("MainWindow", "rasterLayerInfoTab"))
        self.label_26.setText(_translate("MainWindow", "常规信息"))
        self.label_25.setText(_translate("MainWindow", "名称"))
        self.vectorNameLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_32.setText(_translate("MainWindow", "路径"))
        self.vectorSourceLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_30.setText(_translate("MainWindow", "大小合计"))
        self.vectorMemoryLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_34.setText(_translate("MainWindow", "矢量信息"))
        self.label_27.setText(_translate("MainWindow", "范围"))
        self.vectorExtentLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_33.setText(_translate("MainWindow", "几何图形"))
        self.vectorGeoTypeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_31.setText(_translate("MainWindow", "要素总数"))
        self.vectorFeatureNumLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_35.setText(_translate("MainWindow", "编码"))
        self.vectorEncodingLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_28.setText(_translate("MainWindow", "坐标系"))
        self.vectorCrsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_29.setText(_translate("MainWindow", "数据源"))
        self.vectorDpLabel.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vectorLayerInfoTab), _translate("MainWindow", "vectorLayerInfoTab"))
        self.label_2.setText(_translate("MainWindow", "图层渲染"))
        self.pushButton_rasterApply.setText(_translate("MainWindow", "应用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rasterLayerRenderTab), _translate("MainWindow", "layerRenderTab"))
        self.label_36.setText(_translate("MainWindow", "图层渲染"))
        self.vecterRenderCB.setItemText(0, _translate("MainWindow", "单一渲染"))
        self.vecterRenderCB.setItemText(1, _translate("MainWindow", "分类渲染"))
        self.vecterRenderCB.setItemText(2, _translate("MainWindow", "层级渲染"))
        self.comboTabWidget.setTabText(self.comboTabWidget.indexOf(self.singleRender), _translate("MainWindow", "Tab 1"))
        self.comboTabWidget.setTabText(self.comboTabWidget.indexOf(self.categoryRender), _translate("MainWindow", "Tab 2"))
        self.comboTabWidget.setTabText(self.comboTabWidget.indexOf(self.graduatedRender), _translate("MainWindow", "Tab 3"))
        self.pushButton_vectorApply.setText(_translate("MainWindow", "应用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vectorLayerRenderTab), _translate("MainWindow", "vectorLayerRenderTab"))
        self.actionOpenShp.setText(_translate("MainWindow", "打开矢量"))
        self.actionOpenRaster.setText(_translate("MainWindow", "打开栅格"))
        self.actiontest1.setText(_translate("MainWindow", "test1"))
        self.actiontest2.setText(_translate("MainWindow", "test2"))
        self.actiontest3.setText(_translate("MainWindow", "test3"))
import myRc_rc
