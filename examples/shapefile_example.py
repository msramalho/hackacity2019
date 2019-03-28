from ipdb import set_trace          # easy debug
from pprint import pprint as pp     # pretty print things

import geopandas as gpd


# open a shapefile, this example contemplates Portugal's shapefile at the 3rd administrative zone level
shape_file_data = gpd.read_file('templates\\_example_shapefile\\PRT_adm3.shp')

set_trace()
