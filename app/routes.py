from flask import request, Blueprint,  jsonify
import openai
from . import db
from app.models import Question
from app.openai_integration import get_answer


# openai.api_key = app.config['OPENAI_API_KEY']

routes = Blueprint('routes', __name__)

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
        
        # create a new question 
        question_entry = Question(question=question, answer=answer)
        
        db.session.add(question_entry)
        db.session.commit()
        
        return jsonify({'question': question, 'answer': answer})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    
    
    
# def ask_question():
#     data = request.json
#     question_text = data.get('question')
    
#     if not question_text:
#         return jsonify({'error': 'No question provided'}), 400
    
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=question_text,
#         max_tokens=150
#     )
    
#     answer_text = response.choices[0].text.strip()

#     new_question = Question(question=question_text, answer=answer_text)
#     db.session.add(new_question)
#     db.session.commit()

#     return jsonify({'question': question_text, 'answer': answer_text})