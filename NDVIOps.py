import qgis.core 
from qgis.core import *
from qgis.utils import *  
import os, re
import processing
from osgeo import gdal

# importing a raster image 
rasterPathB4 = 'C:/Users/User/Downloads/band 4 red image_export_cog.tif'
rasterPathB5 = 'C:/Users/User/Downloads/band 5 NIR image_export_cog.tif'
B4_layer = QgsRasterLayer(rasterPathB4,"landsat8 band4")
B5_layer = QgsRasterLayer (rasterPathB5, " landsat8 band5")
QgsProject.instance().addMapLayer(B4_layer)
QgsProject.instance().addMapLayer(B5_layer)
#CREATE AN OUTPUT FILE 
outfile = r'C:\Users\User\Desktop\desktop folders\programming\Qgiscodes\New folder\NDVI.tif'

# NDVI calculation 
processing.run("gdal:rastercalculator", 
{'INPUT_A': rasterPathB5,
 'BAND_A':1,
 'INPUT_B': rasterPathB4, 
 'BAND_B':1,
 'FORMULA':'(A-B)/(A+B)',
 'NO_DATA':None,
 'RTYPE':5,
 'OPTIONS':'',
 'EXTRA':'',
 'OUTPUT':outfile
 })
 
NDVI_layer = QgsRasterLayer(outfile,"ndvi")

QgsProject.instance().addMapLayer(NDVI_layer)