from ipdb import set_trace          # easy debug
from pprint import pprint as pp     # pretty print things
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon
from matplotlib import pyplot as plt


import numpy as np
import geopandas as gpd
import utm
import math
import random


# open a shapefile, this example contemplates Portugal's shapefile at the 3rd administrative zone level
# change 3 to 0, 1 or 2 and check the difference in granularity
shape_file_data = gpd.read_file('examples\\_example_shapefile\\PRT_adm2.shp')

# the columns present, typically the most relevant are NAME_* and geometry (where we can get the boundary points)
pp(shape_file_data.columns)


# extract geometry of areas
polygons = shape_file_data['geometry']

# plotting everything
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x_min, x_max = math.inf, -math.inf
y_min, y_max = math.inf, -math.inf
for k in polygons.keys():
    if type(polygons[k]) == MultiPolygon:
        print("MultiPolygon - join sub polygons")
    else:
        lon_poly, lat_poly = polygons[k].exterior.coords.xy
        np_poly = np.array([list(utm.from_latlon(elem[0], elem[1]))[:2] for elem in zip(lat_poly, lon_poly)])
        pgon = plt.Polygon(np_poly, color=(0, 0, 1), alpha=np.random.uniform(0.2, 0.6), zorder=1)
        ax.add_patch(pgon)
        x_min, x_max = min(x_min, np_poly[:, 0].min()), max(x_max, np_poly[:, 0].max())
        y_min, y_max = min(y_min, np_poly[:, 1].min()), max(y_max, np_poly[:, 1].max())


ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
plt.show()
