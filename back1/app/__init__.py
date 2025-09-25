from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, ma, cors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # blueprints
    from .routas.auth import bp as auth_bp
    from .routas.pneus import bp as pneus_bp
    from .routas.veiculos import bp as veiculos_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(pneus_bp, url_prefix='/api/pneus')
    app.register_blueprint(veiculos_bp, url_prefix='/api/veiculos')

    return app
