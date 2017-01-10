"""histogram.py"""

import rasterio
import numpy as np


def histogram(file):
    with rasterio.open(file) as src:
        src = src.read()

    hist, _ = np.histogram(src, bins=256)
    return hist
