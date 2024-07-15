from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f'<Question {self.question_text}>'