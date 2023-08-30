import qgis.core 
from qgis.core import *
from qgis.utils import *  


# importing a raster image 
rasterPath = 'C:/Users/User/Downloads/image_export_cog.tif'
rasterPathCloudClear = 'C:/Users/User/Downloads/image_export_cog_clear.tif'
layer = QgsRasterLayer(rasterPath,"kwanza sub-county")
layerClear = QgsRasterLayer (rasterPathCloudClear, " kwanza subcounty cloud clear")
QgsProject.instance().addMapLayer(layer)
QgsProject.instance().addMapLayer(layerClear)

#layer dimensions
print(layerClear.width(),layerClear.height())

#layer extent
print(layerClear.extent())

#bandcount()
print(layerClear.bandCount())

# get the name of a raster layer for this case the first layer
print(layerClear.bandName(1))

#get available metadata
print(layerClear.metadata())

#######################rendering######################

# get the renderer 
print(layerClear.renderer())

# change the band combinations : eg from green B2 to gereen B5 
layerClear.renderer().setGreenBand(5)
## to cset color on canvas run this line : layerClear.triggerRepaint()

# set back to B2 
layerClear.renderer().setGreenBand(2)
layerClear.triggerRepaint() 
iface.layerTreeView().refreshLayerSymbology(NDVI_layer.id())









