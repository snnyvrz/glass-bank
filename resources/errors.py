class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class ProductAlreadyExistsError(Exception):
    pass


class UpdateProductError(Exception):
    pass


class DeleteProductError(Exception):
    pass


class ProductNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "ProductAlreadyExistsError": {
        "message": "Product with given name already exists",
        "status": 400
    },
    "UpdateProductError": {
        "message": "Updating product added by others is forbidden",
        "status": 403
    },
    "DeleteProductError": {
        "message": "Deleting product added by other is forbidden",
        "status": 403
    },
    "ProductNotExistsError": {
        "message": "Product with given id doesn't exist",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    }
}
