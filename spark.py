"""spark.py"""

from datetime import datetime
from catalogclient.catalog import Catalog
from histogram.histogram import histogram
from pyspark import SparkContext


def join(hist):
    return " ".join([str(i) for i in hist])


def ndvi_files(products):
    prefix = 'file:'

    return [file.filename[len(prefix):] for product in products for file in product.files if
     file.filename.startswith(prefix) and 'NDVI' in file.bands]


products = Catalog().get_products('PROBAV_L3_S5_TOC_100M', 'GEOTIFF',
                                  startdate=datetime(2016, 1, 1), enddate=datetime(2016, 2, 1),
                                  min_lon=2.5, max_lon=6.5, min_lat=49.5, max_lat=51.5)

files = ndvi_files(products)

sc = SparkContext('local[*]', 'python-spark-quickstart')

try:
    hists = sc.parallelize(files).map(histogram)

    for hist in map(join, hists.collect()):
        print hist
finally:
    sc.stop()
