import pprint
import requests
import json
import os
import gmplot
from statistics import mean

# from dataset_bending import get_all_datasets, get_dataset_info, get_dataset_data, display_dataset_polygon


def create_polygons(coordinates, gmap=None, display=False):
    lon, lat = tuple(map(list,zip(*coordinates)))
    gmap = gmplot.GoogleMapPlotter(min(lat), mean(lon), 16) if not gmap else gmap
    gmap.apikey = "AIzaSyA2B83Ome4_S-EXUe5zLTrkaGeZv-Ndft4"
    gmap.polygon(lat, lon, color = 'cornflowerblue') 
    if display: os.system("temp.html")
    return gmap

def display_plot(gmap, filename="temp.html"):
    gmap.draw(filename)
    os.system(filename)

def display_dataset_polygon(dataset):
    gmap = None
    for datapoint in dataset:
        gmap = create_polygons(datapoint["coordinates"][0], gmap)
    display_plot(gmap)

# List all datasets
def get_all_datasets():
    url = "https://opendata.urbanplatform.portodigital.pt/api/3/action/package_list"
    r = requests.get(url)
    return r.json()["result"]

# ### Get Information for custom dataset, by name
# If `url_only` is true, returns location of data, else a tuple of `(dataset-resource, FORMAT, URL)`


def get_dataset_info(dataset, url_only=True):
    # returns a generator for (dataset-resource, FORMAT, URL) or just the URL
    url = "https://opendata.urbanplatform.portodigital.pt/api/3/action/package_show?id=%s" % dataset
    j = requests.get(url).json()
    if not j["success"]:
        print(j["error"])
        return
    for resource in j['result']['resources']:
        if url_only:
            yield resource["url"]
        else:
            yield (resource["name"], resource["format"], resource["url"])

# Get data from url
#  * Set the query params
#  * Specify how to parse result
#  * function to handle request result and return generator of datapoints


DEFAULT_REQ_PARAMS = {'where': "1=1", 'returnGeometry': 'true', 'orderByFields': 'objectid ASC', 'outSR': '4326'}


def remove_useless_from_dict(dic):
    return {k: v for k, v in dic.items() if v and v != " "}


def parse_features_geojson(x):
    features = x["properties"]
    features["coordinates"] = x["geometry"]["coordinates"]
    return remove_useless_from_dict(features)


def parse_features_json(x): return remove_useless_from_dict(x["attributes"])


def get_dataset_data(dataset_url, req_params={"f":"json"}, f="geojson", fields="*"):
    if "fiware" in dataset_url:
        print("API for broker not parsed yet")
        pprint(requests.get(url).json())
    else:
        # default format could be json, but this gives x, y and not lat, lon
        params = DEFAULT_REQ_PARAMS; params.update(req_params); params["f"] = f; params["outFields"]=fields
        data = requests.get(dataset_url + "/query", params=params).json()
        get_attributes = parse_features_geojson if f=="geojson" else parse_features_json
        return map(parse_features_geojson, data["features"])
