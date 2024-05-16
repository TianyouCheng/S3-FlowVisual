# coding: utf-8
from PyQt5.QtCore import Qt
from qgis.gui import QgsDialog, QgsDockWidget
from qgis.gui import QgsColorBox, QgsColorWidget
from qgis.utils import iface
from qgis.core import QgsProject,QgsLayerTreeModel,QgsApplication

# 设置路径为QGIS的安装路径
QgsApplication.setPrefixPath('D:/Software/QGIS/apps/qgis', True)
QgsApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

# 设置一个Qgs应用的索引，第二个参数设为False来禁止GUI
qgs=QgsApplication([],False)


# 加载
qgs.initQgis()

# 这中间写代码
new_dialog = QgsDialog()
new_dialog.resize(200, 200)

color_box = QgsColorBox(new_dialog)


def print_qcolor(qcolor):
    print(qcolor.name())

# Signal inherited from QgsColorWidget
color_box.colorChanged.connect(print_qcolor)

new_dialog.show()

# Change color you want to choose
color_box.setComponent(QgsColorWidget.Blue)

color_box.resize(100, 100)

# Exercice
# Change again the color you can choose.
# Where can you find the available keywords?

# There is a anormal behaviour in the boxes size.
# Try to find out which one?

# Play with QDockWidget
# dock = QgsDockWidget()
# iface.addDockWidget(Qt.RightDockWidgetArea, dock)

# dock.setWidget(color_box)

# new_dialog.destroy()

# 退出
qgs.exec_()
# PROJECT.write("D:/研究生/研一/空间分析软件/测试数据/MYTEST.qgs")
qgs.exitQgis()

