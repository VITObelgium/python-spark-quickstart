"""files.py"""

from catalogclient.catalog import Catalog


def ndvi_files(product_type, start_date, end_date, min_lon, max_lon, min_lat, max_lat):
    products = Catalog().get_products(product_type, 'GEOTIFF', start_date, end_date, min_lon, max_lon, min_lat, max_lat)
    return _ndvi_files(products)


def _ndvi_files(products):
    prefix = 'file:'

    return [file.filename[len(prefix):]
            for product in products
            for file in product.files
            if file.filename.startswith(prefix) and 'NDVI' in file.bands]
