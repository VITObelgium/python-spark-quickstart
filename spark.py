"""spark.py"""

from histogram.histogram import histogram
from pyspark import SparkContext


def files():
    return ['/data/MTDA/TIFFDERIVED/PROBAV_L3_S1_TOC_333M/20160424/PROBAV_S1_TOC_20160424_333M_V001/PROBAV_S1_TOC_X35Y12_20160424_333M_V001_NDVI.tif']


def as_string(hist):
    return " ".join([str(i) for i in hist])


sc = SparkContext('local', 'python-spark-quickstart')

try:
    hists = sc.parallelize(files()).map(histogram)

    for hist in map(as_string, hists.collect()):
        print hist
finally:
    sc.stop()
