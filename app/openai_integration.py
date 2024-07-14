import openai
from flask import current_app as app

def get_answer(question):
    try:
        openai.api_key = app.config['OPENAI_API_KEY']
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=question,
            max_tokens=150
        )
        print(f"OpenAI API response: {response}")
        answer = response.choices[0].text.strip()
        print(f"Extracted answer: {answer}")  # Debugging statement
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        app.logger.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return None
