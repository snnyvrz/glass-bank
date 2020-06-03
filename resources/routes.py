from .product import ProductApi, ProductsApi
from .auth import SignupApi


def initialize_routes(api):
    api.add_resource(ProductsApi, "/api/products")
    api.add_resource(ProductApi, "/api/products/<id>")
    api.add_resource(SignupApi, "/api/auth/signup")
