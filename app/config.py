import os

# Factory pattern 
class Config:
    SQLALCHEMY_DATABASE_URI =  os.getenv('DATABASE_URL')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', "sk-proj-TrVARWLNNUl2kJBRjC0sT3BlbkFJFMlsxjo0UoluKhDECmv1")



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use SQLite in-memory DB for testing

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

