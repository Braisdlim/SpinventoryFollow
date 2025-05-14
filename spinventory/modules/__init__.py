from flask import Flask
from flask_login import LoginManager
from flask_sirope import Sirope

# Inicializar extensiones
login_manager = LoginManager()
sirope = Sirope()

def create_app(config_class='config'):
    """Factory de la aplicación"""
    app = Flask(__name__, instance_relative_config=True)
    
    # Configuración
    app.config.from_object(config_class)
    app.config.from_pyfile('config.py', silent=True)
    
    # Inicializar extensiones
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    sirope.init_app(app)
    
    # Registrar blueprints
    from app.auth.routes import auth_bp
    from app.vinyl.routes import vinyl_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(vinyl_bp)
    
    return app