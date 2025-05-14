from flask import Flask
from modules.auth.routes import auth_bp
from modules.main.routes import main_bp
from flask_login import LoginManager
from sirope import Sirope

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    # Extensiones
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    srp = Sirope(app)
    
    # Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)