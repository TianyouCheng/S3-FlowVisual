from qgis.PyQt import QtCore
from qgis.core import QgsApplication
from PyQt5.QtCore import Qt
import os
import traceback
from Main import MainWindow

if __name__ == '__main__':
    # enviroDir = r"C:\qgis322"
    #os.environ['GDAL_DATA'] = os.path.join(enviroDir, 'share', 'gdal')
    # proj lib
    #os.environ['PROJ_LIB'] = os.path.join(enviroDir, 'share', 'proj')
    # geotiff_csv
    #os.environ['GEOTIFF_CSV'] = os.path.join(enviroDir, 'share', 'epsg_csv')
    #QgsApplication.prefixPath()
    QgsApplication.setPrefixPath('D:/Software/QGIS/apps/qgis', True)
    QgsApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QgsApplication([], True)

    #t = QtCore.QTranslator()
    #t.load(r'.\zh-Hans.qm')
    #app.installTranslator(t)

    app.initQgis()

    mainWindow = MainWindow()
    mainWindow.show()
    #shp = r"D:\111.shp"
    #tif = r"D:\test.tif"
    #mainWindow.addVectorLayer(shp)
    #mainWindow.addRasterLayer(tif)

    app.exec_()
    app.exitQgis()