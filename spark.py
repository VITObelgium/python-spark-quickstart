"""
This sample program uses Apache Spark to calculate a histogram for each PROBA-V tile within a given time range and
bounding box and sums them up - all in parallel.
"""

from datetime import datetime
from operator import add
from histogram.files import ndvi_files
from histogram.histogram import histogram
from pyspark import SparkContext

"""
The code in the __main__ block will be executed on a single node, the 'driver'. It describes the different steps that need
to be executed in parallel.
"""
if __name__ == '__main__':
    """
    Query the PROBA-V files that will be processed. This method returns a simple list of files that match a specific time range and bounding box.
    """
    files = ndvi_files('PROBAV_L3_S1_TOC_333M',
                       start_date=datetime(2016, 1, 1), end_date=datetime(2016, 2, 1),
                       min_lon=2.5, max_lon=6.5, min_lat=49.5, max_lat=51.5)

    #The SparkContext is our entry point to bootstrap parallel operations.
    sc = SparkContext(appName='python-spark-quickstart')

    try:
        #Distribute the local file list over the cluster. In Spark terminology, the result is called an RDD (Resilient Distributed Dataset).
        filesRDD = sc.parallelize(files)
        #Apply the 'histogram' function to each filename using 'map', keep the result in memory using 'cache'.
        hists = filesRDD.map(histogram).cache()
        #Count number of histograms
        count = hists.count()
        #Combine distributed histograms into a single result
        total = list(hists.reduce(lambda h, i: map(add, h, i)))

        print( "sum of %i histograms: %s" % (count, total) )
    finally:
        sc.stop()
