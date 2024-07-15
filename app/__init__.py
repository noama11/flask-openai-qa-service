
from flask import Flask
import os 
from app.models import db

from .config import Config, DevelopmentConfig, TestingConfig, ProductionConfig

from .models import db

from dotenv import load_dotenv

load_dotenv()  

def create_app(config_name='development'):
    load_dotenv() 
    app = Flask(__name__)

    env = os.getenv('FLASK_ENV')
    print(f"Environment: {env}")
    print(env)
    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
   
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)    

    db.init_app(app)
    
    with app.app_context():
        from .routes import routes as routes_blueprint
        app.register_blueprint(routes_blueprint)
        db.create_all()

    return app
