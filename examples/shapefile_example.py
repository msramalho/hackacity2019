from ipdb import set_trace          # easy debug
from pprint import pprint as pp     # pretty print things

import geopandas as gpd


# open a shapefile, this example contemplates Portugal's shapefile at the 3rd administrative zone level
# change 3 to 0, 1 or 2 and check the difference in granularity
shape_file_data = gpd.read_file('examples\\_example_shapefile\\PRT_adm3.shp')

# TODO: plot area for visual confirmation

set_trace()
