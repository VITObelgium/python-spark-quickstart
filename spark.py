"""spark.py"""

from datetime import datetime
from operator import add
from histogram.files import ndvi_files
from histogram.histogram import histogram
from pyspark import SparkContext

if __name__ == '__main__':
    files = ndvi_files('PROBAV_L3_S1_TOC_333M',
                       start_date=datetime(2016, 1, 1), end_date=datetime(2016, 2, 1),
                       min_lon=2.5, max_lon=6.5, min_lat=49.5, max_lat=51.5)

    sc = SparkContext(appName='python-spark-quickstart')

    try:
        hists = sc.parallelize(files).map(histogram)
        sum = hists.reduce(lambda h, i: map(add, h, i))

        print sum
    finally:
        sc.stop()
