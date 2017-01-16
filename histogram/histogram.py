import rasterio
import numpy as np


def histogram(image_file):
    """Calculates the histogram for a given (single band) image file."""

    with rasterio.open(image_file) as src:
        band = src.read()

    hist, _ = np.histogram(band, bins=256)
    return hist
