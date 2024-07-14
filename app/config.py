import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@db:5432/mydatabase"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = "sk-proj-TrVARWLNNUl2kJBRjC0sT3BlbkFJFMlsxjo0UoluKhDECmv1"
