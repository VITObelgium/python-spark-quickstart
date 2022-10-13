from time import time
import numpy as np
from random import random
from operator import add
from pyspark import SparkContext

"""
The code in the __main__ block will be executed on a single node, the 'driver'. It describes the different steps that need
to be executed in parallel.
"""

n = 10000000

def is_point_inside_unit_circle(p):
    # p is useless here
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

if __name__ == '__main__':
    """
    Query the PROBA-V files that will be processed. This method returns a simple list of files that match a specific time range and bounding box.
    """
    #The SparkContext is our entry point to bootstrap parallel operations.
    sc = SparkContext(appName='python-spark-quickstart')

    try:
        t_0 = time()
        count = sc.parallelize(range(0, n)) \
             .map(is_point_inside_unit_circle).reduce(add)
        print(np.round(time()-t_0, 3), "seconds elapsed for spark approach and n=", n)
        print("Pi is roughly %f" % (4.0 * count / n))
    finally:
        sc.stop()
