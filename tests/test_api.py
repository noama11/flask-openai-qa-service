
from unittest.mock import patch
import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def client():
    app = create_app('testing')
    testing_client = app.test_client()
    with app.app_context():
        db.create_all()
    yield testing_client
    with app.app_context():
        db.drop_all()


# testing the end point with correct answer - /ask (post req)
def test_ask_endpoint(client):
    test_question = {"question": "What is the capital of France?"}
    # create mock for the open ai answer
    with patch('app.openai_integration.openai.ChatCompletion.create') as mocked_create:
        mocked_create.return_value = {
            'choices': [{
                'message': {
                    'content': 'Paris'
                }
            }]
        }
        response = client.post('/ask', json=test_question)
        assert response.status_code == 200
        assert 'Paris' in response.get_json()['answer']


# test of openai failure
def test_ask_endpoint_empty_response(client):
    test_question = {"question": "What is the color of the sky on Mars?"}
    with patch('app.openai_integration.openai.ChatCompletion.create') as mocked_create:
        mocked_create.return_value = {
            'choices': [{
                'message': {
                    'content': ''  
                }
            }]
        }
        response = client.post('/ask', json=test_question)
        assert response.status_code == 400  # Expecting a bad request status if no answer can be retrieved
        assert 'error' in response.get_json()
        assert response.get_json()['error'] == 'Could not retrieve answer'
