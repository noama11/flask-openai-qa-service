# from flask_sqlalchemy import SQLAlchemy

from flask import Flask
import os 
from flask import Blueprint  # Import Blueprint
from .config import Config
from app.models import db




def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print(app.config['SQLALCHEMY_DATABASE_URI'])
    
    db.init_app(app)
    
    with app.app_context():
        from .routes import routes as routes_blueprint
        app.register_blueprint(routes_blueprint)
        db.create_all()

    return app
