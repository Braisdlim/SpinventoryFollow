from flask import Flask
from flask_login import LoginManager
from flask_sirope import Sirope

# Inicializar extensiones
login_manager = LoginManager()
sirope = Sirope()

def create_app(config_class='config'):
    """Factory principal de la aplicación"""
    app = Flask(__name__)
    
    # Configuración
    app.config.from_object(config_class)
    
    # Inicializar extensiones con la app
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Ruta de login
    sirope.init_app(app)
    
    # Registrar blueprints
    register_blueprints(app)
    
    # Registrar manejo de errores
    register_error_handlers(app)
    
    return app

def register_blueprints(app):
    """Registra todos los blueprints de la aplicación"""
    from app.auth.routes import bp as auth_bp
    from app.main.routes import bp as main_bp
    from app.vinyl.routes import bp as vinyl_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(vinyl_bp, url_prefix='/vinyl')

def register_error_handlers(app):
    """Registra manejadores de errores"""
    from app.errors.handlers import page_not_found, internal_server_error
    
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)