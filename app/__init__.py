from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from flask import Blueprint  # Import Blueprint
from .config import Config



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    
    with app.app_context():
        from .routes import routes as routes_blueprint
        app.register_blueprint(routes_blueprint)
        db.create_all()

    return app
