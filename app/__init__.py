from flask import Flask
from flask_bootstrap import Bootstrap
from .blueprints.auth import auth, login_manager
from .blueprints.todo_bp import todo_bp
from .db_connection import connect_to_db
import secrets

def create_app():

    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    secret_key = secrets.token_hex(16)
    app.config['SECRET_KEY'] = secret_key
 
    app.register_blueprint(todo_bp)
    app.register_blueprint(auth)
    login_manager.init_app(app)

    bootstrap = Bootstrap(app)
        
    connect_to_db()

    return app