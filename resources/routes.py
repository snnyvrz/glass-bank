from .product import ProductApi, ProductsApi


def initialize_routes(api):
    api.add_resource(ProductsApi, "/api/products")
    api.add_resource(ProductApi, "/api/products/<id>")
