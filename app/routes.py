import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import request, Blueprint,  jsonify
from . import db
from app.models import Question
from app.openai_integration import get_answer
import os


routes = Blueprint('routes', __name__)


@routes.route('/', methods=['GET'])
def home():
    return "Welcome to the homepage!"


@routes.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()

        question = data.get('question')
        print(question)
        answer = get_answer(question)
        
        if not answer:
            return jsonify({'error': 'Could not retrieve answer'}), 400
    
        # create a new question 
        question_entry = Question(question=question, answer=answer)
        
        db.session.add(question_entry)
        db.session.commit()
        
        return jsonify({'question': question, 'answer': answer}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    