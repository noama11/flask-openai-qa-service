from flask import jsonify,  current_app as app
import openai
# from openai.types.chat import ChatCompletion


# or openai.Completion
def get_answer(question):
    try:
        openai.api_key = app.config['OPENAI_API_KEY']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        print(f"OpenAI API response: {response}")
        
        # Return None if the answer is an empty string
        if not answer:
            return None
        
        answer = response.choices[0].text.strip()
        print(f"Extracted answer: {answer}")  # Debugging statement
        return answer
    
    except openai.error.OpenAIError as e:
        app.logger.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return None
