import os
# from dotenv import load_dotenv

# load_dotenv()

# Factory pattern 

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@db:5432/mydatabase"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # OPENAI_API_KEY = "sk-proj-TrVARWLNNUl2kJBRjC0sT3BlbkFJFMlsxjo0UoluKhDECmv1"
    OPENAI_API_KEY = "aa"



class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/test_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use SQLite in-memory DB

class DevelopmentConfig(Config):
    DEBUG = True
    # TESTING = False
    
    # SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'postgresql://dev_user:dev_pass@localhost/dev_db')

# class Config:
#     """Base configuration."""
#     SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')


# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'postgresql://test_user:test_pass@localhost/test_db')

# class ProductionConfig(Config):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://prod_user:prod_pass@localhost/prod_db')
