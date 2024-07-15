# from flask_sqlalchemy import SQLAlchemy

from flask import Flask
import os 
from flask import Blueprint  # Import Blueprint
from app.models import db

# from config import DevelopmentConfig
# from .config import DevelopmentConfig
# from .config import Config
from .config import Config, DevelopmentConfig, TestingConfig

from .models import db

from dotenv import load_dotenv
 # This loads environment variables from .env


def create_app(config_name='development'):
    app = Flask(__name__)
    
    load_dotenv() 
    
    env = os.environ.get('FLASK_ENV', 'development')

    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(TestingConfig)

    # app.config.from_object('app.config.Config')
    # app.config.from_object(config_class)
    
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', config_class.SQLALCHEMY_DATABASE_URI)

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # print(app.config['SQLALCHEMY_DATABASE_URI'])
    
    db.init_app(app)
    
    with app.app_context():
        from .routes import routes as routes_blueprint
        app.register_blueprint(routes_blueprint)
        db.create_all()

    return app
