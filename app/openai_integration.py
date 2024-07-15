from flask import jsonify,  current_app as app
import openai
# from openai.types.chat import ChatCompletion


def get_answer(question):
    try:
        openai.api_key = app.config['OPENAI_API_KEY']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        
        # Log the full response from OpenAI
        app.logger.info(f"OpenAI API response: {response}")

        # Extract and clean the answer text
        if not response['choices'][0]['message']['content'].strip():
            return None
        
        answer = response['choices'][0]['message']['content'].strip()
        
        app.logger.info(f"Extracted answer: {answer}")
        return answer

    except openai.error.OpenAIError as e:
        app.logger.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return None