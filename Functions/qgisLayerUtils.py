from qgis.core import QgsMapLayer,QgsRasterLayer,QgsVectorLayer,QgsProject,QgsRasterDataProvider,QgsVectorDataProvider,QgsCoordinateReferenceSystem,QgsRectangle,QgsWkbTypes,QgsField,QgsFeature
from qgis.gui import QgsMapCanvas
import os
import os.path as osp
import pandas as pd
from Functions.yoyiFile import getFileSize
from Functions.mClass import mFlow,mFlowSet
from PyQt5.QtCore import QVariant
from PyQt5.QtWidgets import QDialog
from UI.Win_CSVRead import Ui_CSVReadDialog

PROJECT = QgsProject.instance()

class WinCSVRead(QDialog,Ui_CSVReadDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def addMapLayer(layer:QgsMapLayer,mapCanvas:QgsMapCanvas,firstAddLayer=False):
    if layer:
        if layer.isValid():
            if firstAddLayer:
                # 缩放到该图层位置
                mapCanvas.setExtent(layer.extent())

            while(PROJECT.mapLayersByName(layer.name())):
                layer.setName(layer.name()+"_1")
            
            PROJECT.addMapLayer(layer)
            layers = [layer] + [PROJECT.mapLayer(i) for i in PROJECT.mapLayers()]
            mapCanvas.setLayers(layers)
            mapCanvas.refresh()

def readRasterFile(rasterFilePath):
    rasterLayer = QgsRasterLayer(rasterFilePath,osp.basename(rasterFilePath))
    return rasterLayer

def readVectorFile(vectorFilePath):
    vectorLayer = QgsVectorLayer(vectorFilePath,osp.basename(vectorFilePath),"ogr")
    return vectorLayer

def readCSVFile(filePath,type):
    """
    均可当作csv文件进行处理.pickle文件需要在文件末尾以_pk进行标识
    :param type: 0为csv文件, 1为pickle文件
    """
    data=fdf=0
    if type==0:
        data = pd.read_csv(filePath,encoding='utf-8')
    elif type==1:
        data = pd.read_pickle(filePath)
    # 使用窗口让其选择经纬度
    CSVReader=WinCSVRead()
    for i in [CSVReader.comboBox,CSVReader.comboBox_2,CSVReader.comboBox_3,CSVReader.comboBox_4]:
        i.addItems(data.columns)
    result=CSVReader.exec_()
    if not result:return
    odlnglat=[CSVReader.comboBox.currentText(),CSVReader.comboBox_2.currentText(),CSVReader.comboBox_3.currentText(),CSVReader.comboBox_4.currentText()]

    # 使用mFlowSet对象处理
    if type==0:
        fdf=mFlowSet.from_file(filePath,
                origin_lng=odlnglat[0],
                origin_lat=odlnglat[1],
                destination_lng=odlnglat[2],
                destination_lat=odlnglat[3])
    elif type==1:
        fdf=mFlowSet.FromPickle_Convert(filePath,
                origin_lng=odlnglat[0],
                origin_lat=odlnglat[1],
                destination_lng=odlnglat[2],
                destination_lat=odlnglat[3])
        
    # Line_Layers.append(fdf)
    # create layer (“point”, “linestring”, “polygon”, “multipoint”,”multilinestring”,”multipolygon”) "memory" name of privider
    filename=os.path.basename(filePath).split('.')[0]
    vl = QgsVectorLayer("linestring", filename, "memory")
    pr = vl.dataProvider()
    # add fields
    for i in fdf.columns:
        if fdf[i].dtype == 'int64':
            pr.addAttributes([QgsField(i,QVariant.Int)])
        elif fdf[i].dtype == 'float64':
            pr.addAttributes([QgsField(i,QVariant.Double)])
        else:
            pr.addAttributes([QgsField(i,QVariant.String)])

    vl.updateFields() # tell the vector layer to fetch changes from the provider
    flowAry=fdf.QGISAry_Convert(odlnglat[0],odlnglat[1],odlnglat[2],odlnglat[3])
    pr.addFeatures(flowAry)
    # update layer's extent when new features have been added
    vl.updateExtents()
    return vl,filename,fdf


qgisDataTypeDict = {
    0 : "UnknownDataType",
    1 : "Uint8",
    2 : "UInt16",
    3 : "Int16",
    4 : "UInt32",
    5 : "Int32",
    6 : "Float32",
    7 : "Float64",
    8 : "CInt16",
    9 : "CInt32",
    10 : "CFloat32",
    11 : "CFloat64",
    12 : "ARGB32",
    13 : "ARGB32_Premultiplied"
}

def getRasterLayerAttrs(rasterLayer:QgsRasterLayer):
    rdp : QgsRasterDataProvider = rasterLayer.dataProvider()
    crs : QgsCoordinateReferenceSystem = rasterLayer.crs()
    extent: QgsRectangle = rasterLayer.extent()
    resDict = {
        "name" : rasterLayer.name(),
        "source" : rasterLayer.source(),
        "memory" : getFileSize(rasterLayer.source()),
        "extent" : f"min:[{extent.xMinimum():.6f},{extent.yMinimum():.6f}]; max:[{extent.xMaximum():.6f},{extent.yMaximum():.6f}]",
        "width" : f"{rasterLayer.width()}",
        "height" : f"{rasterLayer.height()}",
        "dataType" : qgisDataTypeDict[rdp.dataType(1)],
        "bands" : f"{rasterLayer.bandCount()}",
        "crs" : crs.description()
    }
    return resDict

def getVectorLayerAttrs(vectorLayer:QgsVectorLayer):
    vdp : QgsVectorDataProvider = vectorLayer.dataProvider()
    crs: QgsCoordinateReferenceSystem = vectorLayer.crs()
    extent: QgsRectangle = vectorLayer.extent()
    resDict = {
        "name" : vectorLayer.name(),
        "source" : vectorLayer.source(),
        # "memory": getFileSize(vectorLayer.source()),
        "extent" : f"min:[{extent.xMinimum():.6f},{extent.yMinimum():.6f}]; max:[{extent.xMaximum():.6f},{extent.yMaximum():.6f}]",
        "geoType" : QgsWkbTypes.geometryDisplayString(vectorLayer.geometryType()),
        "featureNum" : f"{vectorLayer.featureCount()}",
        "encoding" : vdp.encoding(),
        "crs" : crs.description(),
        "dpSource" : vdp.description()
    }
    return resDict

if __name__ == '__main__':
    shpPath = r"D:/研究生/研一/空间分析软件/测试数据/shp/NetTest.shp"
    shpLayer = readVectorFile(shpPath)
    getVectorLayerAttrs(shpLayer)