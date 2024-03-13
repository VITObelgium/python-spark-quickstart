from terracatalogueclient import Catalogue

def ndvi_files(collection, start_date, end_date, min_lon, max_lon, min_lat, max_lat):
    """Returns a list of NDVI files for a collection of EOProducts specified by a combination of product type,
    time window and bounding box."""
    
    catalogue = Catalogue()
    products = catalogue.get_products(collection, start=start_date, end=end_date, bbox=[min_lon, min_lat, max_lon, max_lat], accessedFrom="MEP")
    return _ndvi_files(products)


def _ndvi_files(products):
    """Returns the list of NDVI files."""

    prefix = 'file://'

    # return [file.filename[len(prefix):] for product in products for file in product.data if 'NDVI' in file]
    return [file.href[len(prefix):] for product in products for file in product.data if "NDVI"==file.title]
