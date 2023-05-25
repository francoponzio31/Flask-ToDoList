from flask import Flask
from flask_bootstrap import Bootstrap
from .blueprints.auth import auth, login_manager
from .blueprints.todo_bp import todo_bp
import os
from dotenv import load_dotenv

def create_app():

    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    load_dotenv()
    app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")
 
    app.register_blueprint(todo_bp)
    app.register_blueprint(auth)
    login_manager.init_app(app)

    bootstrap = Bootstrap(app)

    return app