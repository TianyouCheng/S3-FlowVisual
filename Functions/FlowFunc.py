import pandas as pd
from qgis.core import QgsVectorLayer,QgsPointXY,QgsField,QgsFeature,QgsGeometry
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QColor

def PointFromFlow(data):
    # 传入流datafram文件
    # 根据流节点的度赋予点大小，返回点图层

    # 对称矩阵，所以只用统计O点即统计全部点
    PointSet={} # 点名称和位置
    PointPow={} # 点大小，这里使用流量和
    for index, row in data.iterrows():
        if row['o_ID'] not in PointSet.keys():
            PointSet[row['o_ID']]=(row['o_lng'],row['o_lat'])
            PointPow[row['o_ID']]=0
        else:
            PointPow[row['o_ID']]+=1

    # create layer
    # (“point”, “linestring”, “polygon”, “multipoint”,”multilinestring”,”multipolygon”)
    vl = QgsVectorLayer("point", "flowPoint_test", "memory")
    pr = vl.dataProvider()
    pr.addAttributes([QgsField("FlowCount", QVariant.Int)])
    vl.updateFields()

    for key in PointPow:
        if key=='济南':
            mypoint=QgsPointXY(PointSet[key][0],PointSet[key][1])
            fet=QgsFeature()
            fet.setGeometry(QgsGeometry.fromPointXY(mypoint))
            fet.setAttributes([600])
            pr.addFeatures([fet])
        mypoint=QgsPointXY(PointSet[key][0],PointSet[key][1])
        fet=QgsFeature()
        fet.setGeometry(QgsGeometry.fromPointXY(mypoint))
        fet.setAttributes([PointPow[key]])
        pr.addFeatures([fet])
        
    vl.updateExtents()

    return vl

# def UpdateFlow(scale):
