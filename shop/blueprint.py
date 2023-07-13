from .routes import product_category_bp as ProductCategoryBlueprint
from .routes import product_bp as ProductBlueprint
from .routes import health_bp as HealthBlueprint
from .routes import user_bp as UserBlueprint


def register_routings(app):
    app.register_blueprint(HealthBlueprint)
    app.register_blueprint(ProductBlueprint)
    app.register_blueprint(ProductCategoryBlueprint)
    app.register_blueprint(UserBlueprint)
