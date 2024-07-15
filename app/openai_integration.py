from flask import jsonify,  current_app as app
import openai


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
        if "You exceeded your current quota" in str(e):
            app.logger.error("OpenAI API quota exceeded. Please check your plan and billing details.")
            return "Sorry, we are experiencing high demand. Please try again later."
        else:
            app.logger.error(f"OpenAI API error: {e}")
            return "An error occurred while processing your request."
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return "An unexpected error occurred."