'''
流类，继承 QgsLineString
'''

from qgis.core import QgsLineString, QgsProject, QgsPoint,QgsFeature
import typing
import skmob
from skmob.utils import constants,utils
from skmob.tessellation.tilers import tiler
import geopandas as gpd
from shapely.geometry import Point, Polygon
from pyproj import CRS
import pandas as pd


# 在这里连接起，QGIS的画图类，和软件包的关系
class mFlow(QgsLineString):
    '''
    单条流，继承QgsLineString以画图，可以查询流属性
    :param x1,y1,x2,y2: 为起止点坐标，浮点类型
    :param type: 
    '''
    def __init__(self, x1:float,y1:float,x2:float,y2:float, ) -> None: 
        super().__init__([QgsPoint(x1,y1),QgsPoint(x2,y2)])
        
    def Flow_ODChange1():
        '''
        获取流的长度（欧氏距离）
        '''
        return None
    
    def Flow_ODChange2():
        '''
        改变O或D点位置
        '''
        return None
    
class mFlowSet(skmob.FlowDataFrame):
    '''
    流集合，读入数据专用，继承FlowDataFrame以分析、自动生成起止点，可以查询流之间的距离等操作
    :param x1,y1,x2,y2: 为起止点坐标，浮点类型
    :param type: 
    '''
    def __init__(self,data, origin='origin', destination='destination', flow='flow',
                 datetime='datetime', tile_id='tile_ID', timestamp=False, tessellation=None,
                 parameters={}) -> None:
        super().__init__(data,origin,destination,flow,datetime,tile_id,timestamp,tessellation,parameters)

    def QGISAry_Convert(self,o_lng,o_lat,d_lng,d_lat):
        '''
        转化成QGIS画图支持的QgsLineString列表（mFlow列表）（QgsFeature列表）
        :param o_lng: 字符串，o点的longitude是哪个字段
        '''
        LineFeatureAry=[]
        print(self.columns)
        for index, row in self.iterrows():
            mLine=QgsLineString([QgsPoint(self.tessellation['geometry'][int(self['origin'][index])].x
                        ,self.tessellation['geometry'][int(self['origin'][index])].y)
                        ,QgsPoint(self.tessellation['geometry'][int(self['destination'][index])].x
                        ,self.tessellation['geometry'][int(self['destination'][index])].y)])
            fet=QgsFeature()
            fet.setGeometry(mLine)
            attri=[]
            for i in self.columns:
                attri.append(row[i])
            fet.setAttributes(attri)
            LineFeatureAry.append(fet)
        return LineFeatureAry
    
    @classmethod
    def FromPickle_Convert(cls, filename, encoding=None, origin=None, destination=None, origin_lat=None, origin_lng=None, destination_lat=None,
                  destination_lng=None, flow=constants.FLOW, datetime=constants.DATETIME, timestamp=False, sep=",",
                  tessellation=None, tile_id=constants.TILE_ID, usecols=None, header='infer', parameters=None,
                  remove_na=False):
        '''
        从pickle文件创建类，与from_file(csv)相对应。
        '''
        # Case 1: origin, destination, flow, [datetime]
        if (origin is not None) and (destination is not None):

            if not isinstance(tessellation, gpd.GeoDataFrame):
                raise AttributeError("tessellation must be a GeoDataFrame.")

        df = pd.read_pickle(filename)

        # Case 2: origin_lat, origin_lng, destination_lat, destination_lng, flow, [datetime]
        if (origin_lat is not None) and (origin_lng is not None) and (destination_lat is not None) and \
                (destination_lng is not None):

            # Step 1: if tessellation is None infer it from data
            if tessellation is None:

                a = df[[origin_lat, origin_lng]].rename(columns={origin_lat: 'lat', origin_lng: 'lng'})

                b = df[[destination_lat, destination_lng]].rename(columns={destination_lat: 'lat',
                                                                           destination_lng: 'lng'})

                # DropDuplicates has to be applied now because Geopandas doesn't support removing duplicates in geometry
                points = pd.concat([a, b]).drop_duplicates(['lat', 'lng'])
                points = gpd.GeoDataFrame(geometry=gpd.points_from_xy(points['lng'], points['lat']),
                                          crs=constants.DEFAULT_CRS)

                tessellation = tiler.get('voronoi', points=points)

            # Step 2: map origin and destination points into the tessellation

            gdf_origin = gpd.GeoDataFrame(df.copy(), geometry=gpd.points_from_xy(df[origin_lng], df[origin_lat]),
                                          crs=tessellation.crs)
            gdf_destination = gpd.GeoDataFrame(df.copy(),
                                               geometry=gpd.points_from_xy(df[destination_lng], df[destination_lat]),
                                               crs=tessellation.crs)

            if all(isinstance(x, Polygon) for x in tessellation.geometry):

                if remove_na:
                    how = 'inner'
                else:
                    how = 'left'

                origin_join = gpd.sjoin(gdf_origin, tessellation, how=how, op='within').drop("geometry", axis=1)
                destination_join = gpd.sjoin(gdf_destination, tessellation, how=how, op='within').drop("geometry",
                                                                                                       axis=1)

                df = df.merge(origin_join[[constants.TILE_ID]], left_index=True, right_index=True)
                df.loc[:, constants.ORIGIN] = origin_join[constants.TILE_ID]
                df.drop([constants.ORIGIN_LAT, constants.ORIGIN_LNG, constants.TILE_ID], axis=1, inplace=True)

                df = df.merge(destination_join[[constants.TILE_ID]], left_index=True, right_index=True)
                df.loc[:, constants.DESTINATION] = destination_join[constants.TILE_ID]
                df.drop([constants.DESTINATION_LAT, constants.DESTINATION_LNG, constants.TILE_ID], axis=1, inplace=True)

            elif all(isinstance(x, Point) for x in tessellation.geometry):

                df.loc[:, constants.ORIGIN] = utils.nearest(gdf_origin, tessellation, constants.TILE_ID).values
                df.loc[:, constants.DESTINATION] = utils.nearest(gdf_destination, tessellation,
                                                                 constants.TILE_ID).values

                df.drop([origin_lat, origin_lng, destination_lat, destination_lng], inplace=True, axis=1)

            else:
                raise AttributeError("In case of expanded format (coordinates instead of ids), the tessellation must "
                                     "contains either all Polygon or all Point. Mixed types are not allowed.")

        # Step 3: call the constructor

        if parameters is None:
            parameters = {'from_file': filename}

        return cls(df, origin=constants.ORIGIN, destination=constants.DESTINATION, flow=flow, datetime=datetime,
                   timestamp=timestamp, tessellation=tessellation, parameters=parameters, tile_id=tile_id)


    def Qgiszhuanhua1_Query(self):
        '''
        查询某条流，返回mFlow对象。如果使用流对象进行操作，也基于mFlow对象，因为方便查属性。
        '''
        return None

def Qgiszhuanhua1():
    '''
    把流转化为经纬度坐标
    '''
    return None

if __name__=='__main__':
    # TODO flowset，要其他功能中调用，三种思路，要么储存，要么还原，或者重新读取
    import pandas as pd
    
    data_list = [[1, 39.984094, 116.319236, '2008-10-23 13:53:05'],
 [1, 39.984198, 116.319322, '2008-10-23 13:53:06'],
 [1, 39.984224, 116.319402, '2008-10-23 13:53:11'],
 [1, 39.984211, 116.319389, '2008-10-23 13:53:16']]
    # url_tess = skmob.utils.constants.NY_COUNTIES_2011
    # tessellation = gpd.read_file(url_tess).rename(columns={'tile_id': 'tile_ID'})
    # print(tessellation.head())
    # fdf=mFlowSet(data_list)
    fdf = mFlowSet.from_file("D:/研究生/研一/空间分析软件/测试数据/test_sample_lng.csv",
                                        origin_lat='o_lat',
                                        origin_lng='o_lng',
                                        destination_lat='d_lat',
                                        destination_lng='d_lng')
    # data=pd.read_csv("D:/研究生/研一/空间分析软件/测试数据/test_sample_lng.csv")
    
    # print(data.columns)
    # fdf=mFlowSet(data,
    #             origin_lat='o_lat',
    #             origin_lng='o_lng',
    #             destination_lat='d_lat',
    #             destination_lng='d_lng')
    # print(fdf.head())
    # print(fdf.tessellation['geometry'][0])
    import os
    filepath="D:/研究生/研一/空间分析软件/测试数据/test_sample_lng.csv"
    print(constants.TILE_ID)



