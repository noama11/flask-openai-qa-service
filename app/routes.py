from flask import request, Blueprint,  jsonify
import openai
from . import db
from app.models import Question
from app.openai_integration import get_answer
import os

# openai.api_key = app.config['OPENAI_API_KEY']

routes = Blueprint('routes', __name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
# print(app.config['SQLALCHEMY_DATABASE_URI'])

@routes.route('/', methods=['GET'])
def home():
    return "Welcome to the homepage!"


@routes.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        question = data['question']
        
        # get the answer from openai
        answer = get_answer(question)
        
        if answer is None:
            return jsonify({'error': 'Could not retrieve answer'}), 400
    
        # create a new question 
        question_entry = Question(question=question, answer=answer)
        
        db.session.add(question_entry)
        db.session.commit()
        
        return jsonify({'question': question, 'answer': answer})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    