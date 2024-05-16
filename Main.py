import os,sys,random,cgitb
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QFileDialog,QMessageBox,QTabBar,QListWidgetItem,QGraphicsOpacityEffect
# from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QUrl, QSize, QMimeData,QVariant
from qgis.PyQt import QtCore
from qgis.PyQt.QtWidgets import QMainWindow,QStatusBar,QLabel,QComboBox,QPushButton,QFrame
from qgis.core import QgsProject,QgsLayerTreeModel,QgsApplication,QgsMultiLineString,QgsPoint,QgsPointXY\
    ,QgsLineString,QgsVectorLayer,QgsFeature,QgsGeometry,QgsField,QgsCoordinateReferenceSystem,QgsMapSettings\
    ,QgsMarkerSymbol,QgsRendererCategory,QgsCategorizedSymbolRenderer,QgsRasterLayer,QgsStyle,QgsLayerTreeNode\
    ,QgsLayerTree,QgsWkbTypes
from qgis.gui import QgsLayerTreeView,QgsMapCanvas,QgsLayerTreeMapCanvasBridge,QgsRendererRasterPropertiesWidget\
    ,QgsSingleSymbolRendererWidget,QgsCategorizedSymbolRendererWidget,QgsGraduatedSymbolRendererWidget
from UI.main import Ui_MainWindow
from Functions import WinCSVRead,addMapLayer,readVectorFile,readRasterFile,PointFromFlow,readCSVFile\
    ,getRasterLayerAttrs,getVectorLayerAttrs
from Functions.mClass import mFlow
from Functions.mClass.qgisMenu import menuProvider
import pandas as pd
import os.path as osp
import traceback
import math
import numpy as np
from sklearn.cluster import KMeans
import qdarkstyle
# from UI.ui_main import UI_MainWindow1
from UI.core.json_settings import Settings
from UI.core.functions import Functions
from UI.uis.windows.main_window import *

PROJECT = QgsProject.instance()
class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        # 搜索setGraphicsEffect可取消注释，阴影效果会影响响应速度

        # SETUP MAIN WINDOw
        # Load widgets from "UI\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow1()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # QGIS LOAD
        # ///////////////////////////////////////////////////////////////
        # 1 修改标题
        # self.setWindowTitle("QGIS自定义界面")
        # 2 初始化图层树
        vl = QVBoxLayout(self.ui.right_column.widget)
        self.layerTreeView = QgsLayerTreeView(self)
        self.layerTreeView.setFrameShape(QFrame.NoFrame)
        vl.addWidget(self.layerTreeView)
        # 3 初始化地图画布
        self.mapCanvas = QgsMapCanvas(self)
        hl = QHBoxLayout(self.ui.load_pages.frame)
        self.mapCanvas.setFrameShape(QFrame.NoFrame)
        hl.addWidget(self.mapCanvas)
        # 4 设置图层树风格
        self.model = QgsLayerTreeModel(PROJECT.layerTreeRoot(),self)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeRename) #允许图层节点重命名
        self.model.setFlag(QgsLayerTreeModel.AllowNodeReorder) #允许图层拖拽排序
        self.model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility) #允许改变图层节点可视性
        self.model.setFlag(QgsLayerTreeModel.ShowLegendAsTree) #展示图例
        self.model.setAutoCollapseLegendNodes(10) #当节点数大于等于10时自动折叠
        self.layerTreeView.setModel(self.model)
        # 4 建立图层树与地图画布的桥接
        self.layerTreeBridge = QgsLayerTreeMapCanvasBridge(PROJECT.layerTreeRoot(),self.mapCanvas,self)
        # 5 初始加载影像
        self.firstAdd = True
        # 6 允许拖拽文件
        self.setAcceptDrops(True)
        # 7 图层树右键菜单创建
        self.rightMenuProv = menuProvider(self)
        self.layerTreeView.setMenuProvider(self.rightMenuProv)
        # 8.0 提前给予基本CRS
        self.mapCanvas.setDestinationCrs(QgsCoordinateReferenceSystem("EPSG:3857"))
        # 8 状态栏控件
        XYcoord='{:<40}'.format('')
        self.ui.credits.copyright_label.setText(XYcoord)
        Scale='比例尺'
        self.ui.credits.middle_label.setText(Scale)
        self.ui.credits.middle_combobox.setFixedWidth(120)
        self.ui.credits.middle_combobox.addItems(["1:500","1:1000","1:2500","1:5000","1:10000","1:25000","1:100000","1:500000","1:1000000"])
        self.ui.credits.middle_combobox.setEditable(True)
        CoordSys=f"坐标系: {self.mapCanvas.mapSettings().destinationCrs().description()}-{self.mapCanvas.mapSettings().destinationCrs().authid()}"
        self.ui.credits.version_label.setText(CoordSys)
        btn=self.ui.left_column.findChild(QPushButton, 'style5')
        btn.clicked.connect(self.clicktest)
        # 9 error catch
        self.old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions
        # 10 storage
        self.Line_Layers={}

        # QGIS PROP LOAD
        # ///////////////////////////////////////////////////////////////
        # 1 初始化属性面板的UI
        # layerbar = self.tabWidget.findChild(QTabBar)
        # layerbar.hide()
        # renderBar = self.comboTabWidget.findChild(QTabBar)
        # renderBar.hide()
        # self.listWidget.setCurrentRow(0)

        # 9 底图函数连接


        # 2 动画左右列初始化
        # _translate = QtCore.QCoreApplication.translate
        # self.widget = QtWidgets.QWidget(self.centralwidget)
        # self.widget.setFixedSize(QtCore.QSize(131, 361))
        # self.widget.setObjectName("widget")

        # position = self.widget.pos()
        # self.widget.move(position.x()+40, position.y()+40)
        # self.widget.setStyleSheet("background-color: rgba(25, 35, 45, 0.3);")

        # op=QGraphicsOpacityEffect(self.widget)
        # op.setOpacity(0.3) #0 to 1 will cause the fade effect to kick in
        # self.widget.setGraphicsEffect(op)
        # self.widget.setAutoFillBackground(True)
        

        # self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_1.setGeometry(QtCore.QRect(10, 10, 111, 91))
        # self.pushButton_1.setObjectName("pushButton_1")
        # self.pushButton_1.setStyleSheet("border-image: url(:/img/style1.png);background-color: rgba(25, 35, 45, 0.1)")
        # self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 111, 91))
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_2.setStyleSheet("border-image: url(:/img/style2.png);background-color: rgba(25, 35, 45, 0.1)")
        # self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 111, 91))
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_3.setStyleSheet("border-image: url(:/img/Basemap_Add.png);background-color: rgba(25, 35, 45, 0.1)")
        # self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        # self.widget_2.setFixedSize(QtCore.QSize(131, 361))
        # self.widget_2.setObjectName("widget_2")
        # # self.widget_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        # position = self.widget_2.pos()
        # self.widget_2.move(position.x()+1460, position.y()+40)
        # self.widget_2.setStyleSheet("background-color: rgba(25, 35, 45, 0.3);")
        # # op=QGraphicsOpacityEffect(self.widget_2)
        # # op.setOpacity(0.3) #0 to 1 will cause the fade effect to kick in
        # # self.widget_2.setGraphicsEffect(op)
        # # self.widget_2.setAutoFillBackground(True)

        # self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        # self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 111, 91))
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.pushButton_4.setStyleSheet("border-image: url(:/img/Basemap_Mapbox.png);background-color: rgba(0, 0, 0, 1)")
        # self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        # self.pushButton_5.setGeometry(QtCore.QRect(10, 120, 111, 91))
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.pushButton_5.setStyleSheet("border-image: url(:/img/Basemap_Osm.png)")
        # self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        # self.pushButton_6.setGeometry(QtCore.QRect(10, 230, 111, 91))
        # self.pushButton_6.setObjectName("pushButton_6")
        # self.pushButton_6.setStyleSheet("border-image: url(:/img/Basemap_Add.png);background-color: rgba(25, 35, 45, 0.1);")

    
        
        # A 按钮、菜单栏功能
        self.connectFunc()

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def clicktest(self):
        print(2)

    def btn_clicked(self):
        # GET BT CLICKED
        btnname=self.sender().ActiveObject

        # Remove Selection If Clicked By "btn_close_left_column"
        if btnname != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active         
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        
        # HOME BTN
        if btnname == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btnname)

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # BASEMAP BTN
        if btnname == "btn_basemap":
            # Select Menu
            self.ui.left_menu.select_only_one(btnname)
            # Show / Hide
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
            # Change Left Column Menu
            MainFunctions.set_left_column_menu(
                self, 
                menu = self.ui.left_column.menus.menu_3,
                title = "Basemap tab",
                icon_path = Functions.set_svg_icon("icon_info.svg")
            )

        # LOAD USER PAGE
        if btnname == "btn_add_user":
            # Select Menu
            self.ui.left_menu.select_only_one(btnname)

            # Load Page 3 
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        # LOAD EMPTY PAGE
        if btnname == "btn_TBD":
            # Select Menu
            self.ui.left_menu.select_only_one(btnname)

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # BOTTOM INFORMATION
        if btnname == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btnname)

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btnname)
            else:
                if btnname == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                
                self.ui.left_menu.select_only_one_tab(btnname)

            # Change Left Column Menu
            if btnname != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_2,
                    title = "Info tab",
                    icon_path = Functions.set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btnname == "btn_settings" or btnname == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btnname)
            else:
                if btnname == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btnname)

            # Change Left Column Menu
            if btnname != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings Left Column",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )
        
        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btnname == "btn_top_settings":
            # Toogle Active
            btn=self.ui.title_bar.findChild(QPushButton, btnname)
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)            

        # DEBUG
        print(f"Button {btnname}, clicked!")
        print(btnname)

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btnname=self.sender().ActiveObject

        # DEBUG
        print(f"Button {btnname}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    # QGIS EVENTS
    # ///////////////////////////////////////////////////////////////
    def connectFunc(self):
        #每次移动鼠标，坐标和比例尺变化
        self.mapCanvas.xyCoordinates.connect(self.showXY)
        self.mapCanvas.scaleChanged.connect(self.showScale)
        self.mapCanvas.destinationCrsChanged.connect(self.showCrs)
        self.ui.credits.middle_combobox.editTextChanged.connect(self.changeScaleForString)

        # 树状图关联属性面板
        # self.layerTreeView.clicked.connect(self.Properlayout)
        # self.listWidget.itemClicked.connect(self.listWidgetItemClicked)
        # self.vecterRenderCB.currentIndexChanged.connect(self.vecterRenderCBChanged)

        # action
        # self.actionOpenRaster.triggered.connect(self.actionOpenRasterTriggered)
        # self.actionOpenShp.triggered.connect(self.actionOpenShpTriggered)
        # self.actiontest1.triggered.connect(self.actionTest1)
        # self.actiontest2.triggered.connect(self.actionTest2)
        # self.actiontest3.triggered.connect(self.actionTest3)
        # self.pushButton_vectorApply.clicked.connect(self.renderApplyPbClicked)

        # #=========================================实验性==============================================#
        # # 右侧面板加载底图
        # self.pushButton_4.clicked.connect(lambda: self.Basemap(wmts='Basemap_Mapbox'))
        # self.pushButton_5.clicked.connect(lambda: self.Basemap(wmts='Basemap_Osm'))
        # # 左侧面板加载样式
        # self.pushButton_1.clicked.connect(lambda: self.ApplyStyle(ind=1))
        # self.pushButton_2.clicked.connect(lambda: self.ApplyStyle(ind=2))


    def showXY(self,point):
        x = point.x()
        y = point.y()
        self.ui.credits.copyright_label.setText(f'{x:.6f}, {y:.6f}')

    def showScale(self,scale):
        self.ui.credits.middle_combobox.setEditText(f"1:{int(scale)}")
        #=========================================实验性==============================================#

    def showCrs(self):
        mapSetting : QgsMapSettings = self.mapCanvas.mapSettings()
        self.ui.credits.version_label.setText(f"坐标系: {mapSetting.destinationCrs().description()}-{mapSetting.destinationCrs().authid()}")

    def changeScaleForString(self,str):
        try:
            left,right = str.split(":")[0],str.split(":")[-1]
            if int(left)==1 and int(right)>0 and int(right)!=int(self.mapCanvas.scale()):
                self.mapCanvas.zoomScale(int(right))
                self.mapCanvas.zoomWithCenter()
        except:
            print(traceback.format_stack())

    def dragEnterEvent(self, fileData):
        if fileData.mimeData().hasUrls():
            fileData.accept()
        else:
            fileData.ignore()

    # 拖拽文件事件
    def dropEvent(self,fileData):
        mimeData: QMimeData = fileData.mimeData()
        filePathList = [u.path()[1:] for u in mimeData.urls()]
        for filePath in filePathList:
            filePath:str = filePath.replace("/","//")
            if filePath.split(".")[-1] in ["tif","TIF","tiff","TIFF","GTIFF","png","jpg","pdf"]:
                self.addRasterLayer(filePath)
            elif filePath.split(".")[-1] in ["shp","SHP","gpkg","geojson","kml"]:
                self.addVectorLayer(filePath)
            #=========================================实验性==============================================#
            elif filePath.split(".")[-1] in ["csv"]:
                filePath= filePath.replace("//","/")
                self.addCsvFile(filePath,0)
            elif filePath[-2:]=='pk':
                filePath= filePath.replace("//","/")
                self.addCsvFile(filePath,1)
            elif filePath == "":
                pass
            else:
                QMessageBox.about(self, '警告', f'{filePath}为不支持的文件类型，目前支持栅格影像和shp矢量')
        

    def catch_exceptions(self, ty, value, trace):
        """
            捕获异常，并弹窗显示
        :param ty: 异常的类型
        :param value: 异常的对象
        :param traceback: 异常的traceback
        """
        traceback_format = traceback.format_exception(ty, value, trace)
        traceback_string = "".join(traceback_format)
        QMessageBox.about(self, 'error', traceback_string)
        self.old_hook(ty, value, trace)

    def actionOpenRasterTriggered(self):
        data_file, ext = QFileDialog.getOpenFileName(self, '打开', '','GeoTiff(*.tif;*tiff;*TIF;*TIFF);;All Files(*);;JPEG(*.jpg;*.jpeg;*.JPG;*.JPEG);;*.png;;*.pdf')
        if data_file:
            self.addRasterLayer(data_file)

    def actionOpenShpTriggered(self):
        data_file, ext = QFileDialog.getOpenFileName(self, '打开', '',"ShapeFile(*.shp);;All Files(*);;Other(*.gpkg;*.geojson;*.kml)")
        if data_file:
            self.addVectorLayer(data_file)
        

    def addRasterLayer(self,rasterFilePath):
        rasterLayer = readRasterFile(rasterFilePath)
        if self.firstAdd:
            addMapLayer(rasterLayer,self.mapCanvas,True)
            self.firstAdd = False
        else:
            addMapLayer(rasterLayer,self.mapCanvas)

    def addVectorLayer(self,vectorFilePath):
        vectorLayer = readVectorFile(vectorFilePath)
        if self.firstAdd:
            addMapLayer(vectorLayer,self.mapCanvas,True)
            self.firstAdd = False
        else:
            addMapLayer(vectorLayer,self.mapCanvas)

    def addCsvFile(self,csvFilePath,type):
        vectorLayer,layername,flowset = readCSVFile(csvFilePath,type)
        self.Line_Layers[layername]=flowset
        if self.firstAdd:
            addMapLayer(vectorLayer,self.mapCanvas,True)
            self.firstAdd = False
        else:
            addMapLayer(vectorLayer,self.mapCanvas)
        self.mapCanvas.setExtent(vectorLayer.extent())
        self.mapCanvas.refresh()


    def renderApplyPbClicked(self):
        node: QgsLayerTreeNode = self.layerTreeView.currentNode()
        if self.tabWidget.currentIndex() <= 1 or not(QgsLayerTree.isLayer(node)):
            print("没有在视图里，啥也不干")
        elif type(self.layerTreeView.selectedLayers()[0]) == QgsRasterLayer:
            self.rasterRenderWidget : QgsRendererRasterPropertiesWidget
            self.rasterRenderWidget.apply()
        elif type(self.layerTreeView.selectedLayers()[0]) == QgsVectorLayer:
            print("矢量渲染")
            #self.vectorRenderWidget : QgsSingleSymbolRendererWidget
            layer=self.layerTreeView.selectedLayers()[0]
            layer : QgsVectorLayer
            if self.comboTabWidget.currentIndex() == 0:
                renderer = self.vectorSingleRenderWidget.renderer()
            elif self.comboTabWidget.currentIndex() == 1:
                renderer = self.vectorCateGoryRenderWidget.renderer()
            elif self.comboTabWidget.currentIndex() == 2:
                renderer = self.vectorGraduatedRenderWidget.renderer()
            layer.setRenderer(renderer)
            layer.triggerRepaint()
        self.mapCanvas.refresh()
        
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        # 1 修改标题
        self.setWindowTitle("QGIS自定义界面")
        # 2 初始化图层树
        vl = QVBoxLayout(self.dockWidgetContents)
        self.layerTreeView = QgsLayerTreeView(self)
        vl.addWidget(self.layerTreeView)
        # 3 初始化地图画布
        self.mapCanvas = QgsMapCanvas(self)
        hl = QHBoxLayout(self.frame)
        hl.setContentsMargins(0,0,0,0) #设置周围间距
        hl.addWidget(self.mapCanvas)
        # 4 设置图层树风格
        self.model = QgsLayerTreeModel(PROJECT.layerTreeRoot(),self)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeRename) #允许图层节点重命名
        self.model.setFlag(QgsLayerTreeModel.AllowNodeReorder) #允许图层拖拽排序
        self.model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility) #允许改变图层节点可视性
        self.model.setFlag(QgsLayerTreeModel.ShowLegendAsTree) #展示图例
        self.model.setAutoCollapseLegendNodes(10) #当节点数大于等于10时自动折叠
        self.layerTreeView.setModel(self.model)
        # 4 建立图层树与地图画布的桥接
        self.layerTreeBridge = QgsLayerTreeMapCanvasBridge(PROJECT.layerTreeRoot(),self.mapCanvas,self)
        # 5 初始加载影像
        self.firstAdd = True
        # 6 允许拖拽文件
        self.setAcceptDrops(True)
        # 7 图层树右键菜单创建
        self.rightMenuProv = menuProvider(self)
        self.layerTreeView.setMenuProvider(self.rightMenuProv)

        # 8.0 提前给予基本CRS
        self.mapCanvas.setDestinationCrs(QgsCoordinateReferenceSystem("EPSG:3857"))

        # 8 状态栏控件
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet('color: black; border: none')
        self.statusXY = QLabel('{:<40}'.format('')) #x y 坐标状态
        self.statusBar.addWidget(self.statusXY,1)

        self.statusScaleLabel = QLabel('比例尺')
        self.statusScaleComboBox = QComboBox(self)
        self.statusScaleComboBox.setFixedWidth(120)
        self.statusScaleComboBox.addItems(["1:500","1:1000","1:2500","1:5000","1:10000","1:25000","1:100000","1:500000","1:1000000"])
        self.statusScaleComboBox.setEditable(True)
        self.statusBar.addWidget(self.statusScaleLabel)
        self.statusBar.addWidget(self.statusScaleComboBox)

        self.statusCrsLabel = QLabel(f"坐标系: {self.mapCanvas.mapSettings().destinationCrs().description()}-{self.mapCanvas.mapSettings().destinationCrs().authid()}")
        self.statusBar.addWidget(self.statusCrsLabel)

        self.setStatusBar(self.statusBar)

        # 9 error catch
        self.old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions

        # 10 storage
        self.Line_Layers={}


        #=========================================实验性==============================================#
        self.pointlayertest=0
        
        # 1 初始化属性面板的UI
        layerbar = self.tabWidget.findChild(QTabBar)
        layerbar.hide()
        renderBar = self.comboTabWidget.findChild(QTabBar)
        renderBar.hide()
        self.listWidget.setCurrentRow(0)

        # 2 动画左右列初始化
        _translate = QtCore.QCoreApplication.translate
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setFixedSize(QtCore.QSize(131, 361))
        self.widget.setObjectName("widget")

        position = self.widget.pos()
        self.widget.move(position.x()+40, position.y()+40)
        self.widget.setStyleSheet("background-color: rgba(25, 35, 45, 0.3);")

        # op=QGraphicsOpacityEffect(self.widget)
        # op.setOpacity(0.3) #0 to 1 will cause the fade effect to kick in
        # self.widget.setGraphicsEffect(op)
        # self.widget.setAutoFillBackground(True)
        

        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 10, 111, 91))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setStyleSheet("border-image: url(:/img/style1.png);background-color: rgba(25, 35, 45, 0.1)")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 111, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("border-image: url(:/img/style2.png);background-color: rgba(25, 35, 45, 0.1)")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 111, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("border-image: url(:/img/Basemap_Add.png);background-color: rgba(25, 35, 45, 0.1)")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setFixedSize(QtCore.QSize(131, 361))
        self.widget_2.setObjectName("widget_2")
        # self.widget_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        position = self.widget_2.pos()
        self.widget_2.move(position.x()+1460, position.y()+40)
        self.widget_2.setStyleSheet("background-color: rgba(25, 35, 45, 0.3);")
        # op=QGraphicsOpacityEffect(self.widget_2)
        # op.setOpacity(0.3) #0 to 1 will cause the fade effect to kick in
        # self.widget_2.setGraphicsEffect(op)
        # self.widget_2.setAutoFillBackground(True)

        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 111, 91))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("border-image: url(:/img/Basemap_Mapbox.png);background-color: rgba(0, 0, 0, 1)")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 120, 111, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("border-image: url(:/img/Basemap_Osm.png)")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 230, 111, 91))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("border-image: url(:/img/Basemap_Add.png);background-color: rgba(25, 35, 45, 0.1);")

    
        
        # A 按钮、菜单栏功能
        self.connectFunc()

    def connectFunc(self):
        #每次移动鼠标，坐标和比例尺变化
        self.mapCanvas.xyCoordinates.connect(self.showXY)
        self.mapCanvas.scaleChanged.connect(self.showScale)
        self.mapCanvas.destinationCrsChanged.connect(self.showCrs)
        self.statusScaleComboBox.editTextChanged.connect(self.changeScaleForString)

        # 树状图关联属性面板
        self.layerTreeView.clicked.connect(self.Properlayout)
        self.listWidget.itemClicked.connect(self.listWidgetItemClicked)
        self.vecterRenderCB.currentIndexChanged.connect(self.vecterRenderCBChanged)

        # action
        self.actionOpenRaster.triggered.connect(self.actionOpenRasterTriggered)
        self.actionOpenShp.triggered.connect(self.actionOpenShpTriggered)
        self.actiontest1.triggered.connect(self.actionTest1)
        self.actiontest2.triggered.connect(self.actionTest2)
        self.actiontest3.triggered.connect(self.actionTest3)
        self.pushButton_vectorApply.clicked.connect(self.renderApplyPbClicked)

        #=========================================实验性==============================================#
        # 右侧面板加载底图
        self.pushButton_4.clicked.connect(lambda: self.Basemap(wmts='Basemap_Mapbox'))
        self.pushButton_5.clicked.connect(lambda: self.Basemap(wmts='Basemap_Osm'))
        # 左侧面板加载样式
        self.pushButton_1.clicked.connect(lambda: self.ApplyStyle(ind=1))
        self.pushButton_2.clicked.connect(lambda: self.ApplyStyle(ind=2))


    def showXY(self,point):
        x = point.x()
        y = point.y()
        self.statusXY.setText(f'{x:.6f}, {y:.6f}')

    def showScale(self,scale):
        self.statusScaleComboBox.setEditText(f"1:{int(scale)}")
        #=========================================实验性==============================================#


    def showCrs(self):
        mapSetting : QgsMapSettings = self.mapCanvas.mapSettings()
        self.statusCrsLabel.setText(f"坐标系: {mapSetting.destinationCrs().description()}-{mapSetting.destinationCrs().authid()}")

    def changeScaleForString(self,str):
        try:
            left,right = str.split(":")[0],str.split(":")[-1]
            if int(left)==1 and int(right)>0 and int(right)!=int(self.mapCanvas.scale()):
                self.mapCanvas.zoomScale(int(right))
                self.mapCanvas.zoomWithCenter()
        except:
            print(traceback.format_stack())

    def dragEnterEvent(self, fileData):
        if fileData.mimeData().hasUrls():
            fileData.accept()
        else:
            fileData.ignore()

    # 拖拽文件事件
    def dropEvent(self,fileData):
        mimeData: QMimeData = fileData.mimeData()
        filePathList = [u.path()[1:] for u in mimeData.urls()]
        for filePath in filePathList:
            filePath:str = filePath.replace("/","//")
            if filePath.split(".")[-1] in ["tif","TIF","tiff","TIFF","GTIFF","png","jpg","pdf"]:
                self.addRasterLayer(filePath)
            elif filePath.split(".")[-1] in ["shp","SHP","gpkg","geojson","kml"]:
                self.addVectorLayer(filePath)
            #=========================================实验性==============================================#
            elif filePath.split(".")[-1] in ["csv"]:
                filePath= filePath.replace("//","/")
                self.addCsvFile(filePath,0)
            elif filePath[-2:]=='pk':
                filePath= filePath.replace("//","/")
                self.addCsvFile(filePath,1)
            elif filePath == "":
                pass
            else:
                QMessageBox.about(self, '警告', f'{filePath}为不支持的文件类型，目前支持栅格影像和shp矢量')
    
    def catch_exceptions(self, ty, value, trace):
        """
            捕获异常，并弹窗显示
        :param ty: 异常的类型
        :param value: 异常的对象
        :param traceback: 异常的traceback
        """
        traceback_format = traceback.format_exception(ty, value, trace)
        traceback_string = "".join(traceback_format)
        QMessageBox.about(self, 'error', traceback_string)
        self.old_hook(ty, value, trace)

    def actionOpenRasterTriggered(self):
        data_file, ext = QFileDialog.getOpenFileName(self, '打开', '','GeoTiff(*.tif;*tiff;*TIF;*TIFF);;All Files(*);;JPEG(*.jpg;*.jpeg;*.JPG;*.JPEG);;*.png;;*.pdf')
        if data_file:
            self.addRasterLayer(data_file)

    def actionOpenShpTriggered(self):
        data_file, ext = QFileDialog.getOpenFileName(self, '打开', '',"ShapeFile(*.shp);;All Files(*);;Other(*.gpkg;*.geojson;*.kml)")
        if data_file:
            self.addVectorLayer(data_file)
        

    def addRasterLayer(self,rasterFilePath):
        rasterLayer = readRasterFile(rasterFilePath)
        if self.firstAdd:
            addMapLayer(rasterLayer,self.mapCanvas,True)
            self.firstAdd = False
        else:
            addMapLayer(rasterLayer,self.mapCanvas)

    def addVectorLayer(self,vectorFilePath):
        vectorLayer = readVectorFile(vectorFilePath)
        if self.firstAdd:
            addMapLayer(vectorLayer,self.mapCanvas,True)
            self.firstAdd = False
        else:
            addMapLayer(vectorLayer,self.mapCanvas)

    def addCsvFile(self,csvFilePath,type):
        vectorLayer,layername,flowset = readCSVFile(csvFilePath,type)
        self.Line_Layers[layername]=flowset
        if self.firstAdd:
            addMapLayer(vectorLayer,self.mapCanvas,True)
            self.firstAdd = False
        else:
            addMapLayer(vectorLayer,self.mapCanvas)


    def renderApplyPbClicked(self):
        node: QgsLayerTreeNode = self.layerTreeView.currentNode()
        if self.tabWidget.currentIndex() <= 1 or not(QgsLayerTree.isLayer(node)):
            print("没有在视图里，啥也不干")
        elif type(self.layerTreeView.selectedLayers()[0]) == QgsRasterLayer:
            self.rasterRenderWidget : QgsRendererRasterPropertiesWidget
            self.rasterRenderWidget.apply()
        elif type(self.layerTreeView.selectedLayers()[0]) == QgsVectorLayer:
            print("矢量渲染")
            #self.vectorRenderWidget : QgsSingleSymbolRendererWidget
            layer=self.layerTreeView.selectedLayers()[0]
            layer : QgsVectorLayer
            if self.comboTabWidget.currentIndex() == 0:
                renderer = self.vectorSingleRenderWidget.renderer()
            elif self.comboTabWidget.currentIndex() == 1:
                renderer = self.vectorCateGoryRenderWidget.renderer()
            elif self.comboTabWidget.currentIndex() == 2:
                renderer = self.vectorGraduatedRenderWidget.renderer()
            layer.setRenderer(renderer)
            layer.triggerRepaint()
        self.mapCanvas.refresh()



    #=========================================实验性==============================================#
    def Properlayout(self):
        layer=0
        node: QgsLayerTreeNode = self.layerTreeView.currentNode()
        if QgsLayerTree.isLayer(node):
            layer=self.layerTreeView.selectedLayers()[0]
            index = self.listWidget.currentRow()
            self.decideRasterNVector(index)
            
        if type(layer) == QgsRasterLayer:
            rasterLayerDict = getRasterLayerAttrs(layer)
            self.rasterNameLabel.setText(rasterLayerDict['name'])
            self.rasterSourceLabel.setText(rasterLayerDict['source'])
            # self.rasterMemoryLabel.setText(rasterLayerDict['memory'])
            self.rasterExtentLabel.setText(rasterLayerDict['extent'])
            self.rasterWidthLabel.setText(rasterLayerDict['width'])
            self.rasterHeightLabel.setText(rasterLayerDict['height'])
            self.rasterDataTypeLabel.setText(rasterLayerDict['dataType'])
            self.rasterBandNumLabel.setText(rasterLayerDict['bands'])
            self.rasterCrsLabel.setText(rasterLayerDict['crs'])
            self.rasterRenderWidget = QgsRendererRasterPropertiesWidget(layer, self.mapCanvas,parent=self)
            if self.layerRenderLayout.count():
                self.layerRenderLayout.itemAt(0).widget().deleteLater()
            self.layerRenderLayout.addWidget(self.rasterRenderWidget)
        elif type(layer) == QgsVectorLayer:
            vectorLayerDict = getVectorLayerAttrs(layer)
            self.vectorNameLabel.setText(vectorLayerDict['name'])
            self.vectorSourceLabel.setText(vectorLayerDict['source'])
            # self.vectorMemoryLabel.setText(vectorLayerDict['memory'])
            self.vectorExtentLabel.setText(vectorLayerDict['extent'])
            self.vectorGeoTypeLabel.setText(vectorLayerDict['geoType'])
            self.vectorFeatureNumLabel.setText(vectorLayerDict['featureNum'])
            self.vectorEncodingLabel.setText(vectorLayerDict['encoding'])
            self.vectorCrsLabel.setText(vectorLayerDict['crs'])
            self.vectorDpLabel.setText(vectorLayerDict['dpSource'])

            # single Render
            self.vectorSingleRenderWidget = QgsSingleSymbolRendererWidget(layer,QgsStyle.defaultStyle(),layer.renderer())
            if self.singleRenderLayout.count():
                self.singleRenderLayout.itemAt(0).widget().deleteLater()
            self.singleRenderLayout.addWidget(self.vectorSingleRenderWidget)

            # category Render
            self.vectorCateGoryRenderWidget = QgsCategorizedSymbolRendererWidget(layer,QgsStyle.defaultStyle(),layer.renderer())
            if self.cateRenderLayout.count():
                self.cateRenderLayout.itemAt(0).widget().deleteLater()
            self.cateRenderLayout.addWidget(self.vectorCateGoryRenderWidget)

            # graduated Render
            self.vectorGraduatedRenderWidget=QgsGraduatedSymbolRendererWidget(layer,QgsStyle.defaultStyle(),layer.renderer())
            if self.gradRenderLayout.count():
                self.gradRenderLayout.itemAt(0).widget().deleteLater()
            self.gradRenderLayout.addWidget(self.vectorGraduatedRenderWidget)

    def decideRasterNVector(self,index):
        layer=self.layerTreeView.selectedLayers()[0]
        if index == 0:
            if type(layer) == QgsRasterLayer:
                self.tabWidget.setCurrentIndex(0)
            elif type(layer) == QgsVectorLayer:
                self.tabWidget.setCurrentIndex(1)
        elif index == 1:
            if type(layer) == QgsRasterLayer:
                self.tabWidget.setCurrentIndex(2)
            elif type(layer) == QgsVectorLayer:
                self.tabWidget.setCurrentIndex(3)

    def listWidgetItemClicked(self):
        layer=0
        node: QgsLayerTreeNode = self.layerTreeView.currentNode()
        if QgsLayerTree.isLayer(node):
            layer=self.layerTreeView.selectedLayers()[0]
            index = self.listWidget.currentRow()
            self.decideRasterNVector(index)
    
    def vecterRenderCBChanged(self):
        self.comboTabWidget.setCurrentIndex(self.vecterRenderCB.currentIndex())

    def Basemap(self,wmts):
        layers = QgsProject.instance().mapLayers()
        for layer_id, layer in layers.items():
            if 'Basemap' in layer.name():
                PROJECT.removeMapLayer(layer)
                self.mapCanvas.refresh()
                break

        urlWithParams = 'http-header:referer=&tilePixelRatio=1&type=xyz&url=https://api.mapbox.com/styles/v1/mapbox/light-v11/tiles/256/%7Bz%7D/%7Bx%7D/%7By%7D@2x?access_token%3Dpk.eyJ1IjoiMzA1NzU4MDI2OCIsImEiOiJja3R3dTU4Ym8ybmoyMnhwbWZ1ZnZ5c3BwIn0.n0dPOKbtOpE-QP3XZhgzSQ&zmax=4&zmin=0'
        rlayer=0
        if wmts=='Basemap_Mapbox':
            urlWithParams = 'http-header:referer=&tilePixelRatio=1&type=xyz&url=https://api.mapbox.com/styles/v1/mapbox/light-v11/tiles/256/%7Bz%7D/%7Bx%7D/%7By%7D@2x?access_token%3Dpk.eyJ1IjoiMzA1NzU4MDI2OCIsImEiOiJja3R3dTU4Ym8ybmoyMnhwbWZ1ZnZ5c3BwIn0.n0dPOKbtOpE-QP3XZhgzSQ&zmax=4&zmin=0'
        elif wmts=='Basemap_Osm':
            urlWithParams = 'type=xyz&url=https://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=5&zmin=0'

        rlayer = QgsRasterLayer(urlWithParams, wmts, 'wms')  
        QgsProject.instance().addMapLayer(rlayer)

    def ApplyStyle(self,ind):    
        layers = QgsProject.instance().mapLayers()
        for layer_id, layer in layers.items():
            if type(layer)==QgsVectorLayer:
                if layer.geometryType()==QgsWkbTypes.LineGeometry:
                    pathqml='style/style'+str(ind)+'.qml'
                    layer.loadNamedStyle(pathqml)
                    layer.triggerRepaint()



    def actionTest1(self):
        # https://gis.stackexchange.com/questions/355317/define-categorized-renderer-with-symbols-based-on-several-categories
        # 设置大小不同的符号
        # create a new symbol
        # layer=PROJECT.instance().mapLayersByName('flowPoint_test')[0]

        # feats=[feat for feat in layer.getFeatures()]
        # n=len(feats)

        # field_name=layer.fields().indexFromName('FlowCount')
        # unique_freq=layer.uniqueValues(field_name)
        # # idx=fields_names.index('FlowCount')
        # categories=[]
        # for i in unique_freq:
        #     marker_symbol=QgsMarkerSymbol.createSimple({'size':str(i/50)})
        #     category=QgsRendererCategory(i,marker_symbol.clone(),str(i))
        #     categories.append(category)

        # renderer = QgsCategorizedSymbolRenderer("FlowCount", categories)
        # layer.setRenderer(renderer)
        # # repaint the layer
        # layer.triggerRepaint()

        # 2024/03/27 测试流绑定
        # 读入流的信息
        # layer=PROJECT.instance().mapLayersByName('test_sample_pk')[0]
        # feats=[feat for feat in layer.getFeatures()]
        # print(feats[0].test)
        print(self.Line_Layers)

    def actionTest2(self):
        # 修改策略，把点移动到一起，缩小是再移回去
        layer=PROJECT.instance().mapLayersByName('flowPoint_test')[0]
        # layer=PROJECT.instance().mapLayersByName('flow_test')[0]

        feats=[feat for feat in layer.getFeatures()]
        n=len(feats)
            

        scale=37385391673000
        scaleAry=[10**i for i in range(11,15)]
        scaleAry=np.array(scaleAry)
        scale_factor=int(14-(math.log(min(scaleAry[scale<scaleAry]),10))) #0，1，2，3的情况下是最细化，全部点
            
        pointnum=n
        yu=(pointnum-2)%3
        jiange=math.floor((pointnum-2)/3)
        # 最大尺度下的点个数为2+yu
        # 其他五个尺度的点个数为最大+jiange
        pointary=[2+yu+jiange*i for i in range(4)] #pointary和scale_factor一一对应
        n_clusters=pointary[scale_factor]
        xy=[]
        voldic={}
        voldic_sum={}

        idx=layer.fields().indexFromName('FlowCount')
        for i in range(pointnum):
            xy.append([feats[i].geometry().asPoint().x(),feats[i].geometry().asPoint().y()])
            voldic[i]=feats[i].attributes()[idx]
        
        self.pointlayertest=xy
        # xy=[[random.random()*100,random.random()*100] for i in range(41)]

        model=KMeans(n_clusters=n_clusters).fit(xy)
        y_pred=model.labels_
        # print(y_pred)
        cluster_point={}
        for i in range(pointnum):
            if y_pred[i] not in cluster_point:
                cluster_point[y_pred[i]]=i
                voldic_sum[y_pred[i]]=feats[i].attributes()[idx]
            else:
                if voldic[i]>voldic[cluster_point[y_pred[i]]]:
                    cluster_point[y_pred[i]]=i
                    voldic_sum[y_pred[i]]+=feats[i].attributes()[idx]
        
        # print(cluster_point)


        layer.dataProvider().addAttributes([QgsField("FlowCount_scale", QVariant.Int)])
        layer.updateFields()
        field_name=layer.fields().indexFromName('FlowCount_scale')

        for i in range(n):
            geom=feats[i].geometry()
            geom.moveVertex(xy[cluster_point[y_pred[i]]][0],xy[cluster_point[y_pred[i]]][1],0)

            fid=feats[i].id()
            attr_value = {field_name:voldic_sum[y_pred[i]]}
            layer.dataProvider().changeAttributeValues({fid:attr_value})
            layer.dataProvider().changeGeometryValues({fid:geom})

        unique_freq=layer.uniqueValues(field_name)
        categories=[]
        for i in unique_freq:
            marker_symbol=QgsMarkerSymbol.createSimple({'size':str(i/80)})
            category=QgsRendererCategory(i,marker_symbol.clone(),str(i))
            categories.append(category)

        renderer = QgsCategorizedSymbolRenderer("FlowCount_scale", categories)
        layer.setRenderer(renderer)
        # repaint the layer
        layer.triggerRepaint()
        
    def actionTest3(self):
        layers = QgsProject.instance().mapLayers()
        for layer_id, layer in layers.items():
            if type(layer)==QgsVectorLayer:
                if layer.geometryType()==QgsWkbTypes.LineGeometry:
                    pathqml='style/linestring.qml'
                    layer.saveNamedStyle(pathqml)

        # layers = QgsProject.instance().mapLayers()
        # for layer_id, layer in layers.items():
        #     if type(layer)==QgsVectorLayer:
        #         if layer.geometryType()==QgsWkbTypes.LineGeometry:
        #             name=layer.name()
        #             pathqml='style/linestring.qml'
        #             layer.loadNamedStyle(pathqml)
        #             layer.triggerRepaint()
                    
        # TODO
        # 第一个按钮，分类渲染，设置符号层级
        # 第二个按钮，弯曲线条
        # 最后弄好Layers of detail就结束了

        


        


if __name__=='__main__':
    # 设置路径为QGIS的安装路径
    QgsApplication.setPrefixPath('D:/Software/QGIS/apps/qgis', True)
    QgsApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    # 设置一个Qgs应用的索引，第二个参数设为False来禁止GUI
    qgs=QgsApplication([],False)

    # 安装翻译
    trans=QtCore.QTranslator()
    trans.load(r'./zh-Hans.qm')
    qgs.installTranslator(trans)

    # 加载
    qgs.initQgis()

    # 这中间写代码
    mainWin=MainWindow1()
    # mainWin.setWindowState(Qt.WindowMaximized)
    # mainWin.show()
    # PROJECT.read("D:/研究生/研一/空间分析软件/测试数据/MYTEST.qgs")

    # qgs.setStyleSheet(qdarkstyle.load_stylesheet())
    # urlWithParams = 'type=xyz&url=https://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0'
    # urlWithParams = 'http-header:referer=&tilePixelRatio=1&type=xyz&url=https://api.mapbox.com/styles/v1/mapbox/light-v11/tiles/256/%7Bz%7D/%7Bx%7D/%7By%7D@2x?access_token%3Dpk.eyJ1IjoiMzA1NzU4MDI2OCIsImEiOiJja3R3dTU4Ym8ybmoyMnhwbWZ1ZnZ5c3BwIn0.n0dPOKbtOpE-QP3XZhgzSQ&zmax=4&zmin=0'
    # rlayer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')  

    # if rlayer.isValid():
    #     QgsProject.instance().addMapLayer(rlayer)
    # else:
    #     print('invalid layer')
    # crs = rlayer.crs()
    # crs.createFromId(3857)
    # mainWin.mapCanvas.setDestinationCrs(rlayer.crs())
    # mainWin.mapCanvas.setMapUnits(QGis.Degrees)

    # mainWin.mapCanvas.refresh()
    

    
    # PROJECT.read("D:/研究生/研一/空间分析软件/测试数据/MYTEST.qgs")
    # PROJECT.write("D:/研究生/研一/空间分析软件/测试数据/MYTEST.qgs")

    # 退出
    qgs.exec_()
    # PROJECT.write("D:/研究生/研一/空间分析软件/测试数据/MYTEST.qgs")
    qgs.exitQgis()

