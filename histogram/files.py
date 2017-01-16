from catalogclient.catalog import Catalog


def ndvi_files(product_type, start_date, end_date, min_lon, max_lon, min_lat, max_lat):
    """Returns a list of NDVI files for a collection of EOProducts specified by a combination of product type,
    time window and bounding box."""

    products = Catalog().get_products(product_type, 'GEOTIFF', start_date, end_date, min_lon, max_lon, min_lat, max_lat)
    return _ndvi_files(products)


def _ndvi_files(products):
    """Returns the list of NDVI files within a collection of EOProducts."""

    prefix = 'file:'

    return [file.filename[len(prefix):]
            for product in products
            for file in product.files
            if file.filename.startswith(prefix) and 'NDVI' in file.bands]
