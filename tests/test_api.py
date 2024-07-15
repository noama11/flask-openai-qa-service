# import pytest
# from flask_testing import TestCase
# from app import create_app, db
# from app.models import Question

# class TestFlaskApi(TestCase):
#     def create_app(self):
#         # Use the testing configuration
#         return create_app('TestingConfig')

#     def setUp(self):
#         # Setup your database here if needed
#         db.create_all()

#     def tearDown(self):
#         # Tear down and clean up the database after tests
#         db.session.remove()
#         db.drop_all()

#     def test_ask_endpoint(self):
#         # Prepare the data payload for the POST request
#         test_question = {"question": "What is the capital of France?"}
#         # Use the test client to send a POST request
#         response = self.client.post('/ask', json=test_question)
        
#         # Assert checks
#         assert response.status_code == 200
#         assert b"Paris" in response.data  # Assuming "Paris" would be the correct answer

# # Run the tests
# if __name__ == '__main__':
#     pytest.main(['-v', 'test_api.py'])  # Verbose mode for more details

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
                    'content': ''  # Simulating an empty answer
                }
            }]
        }
        response = client.post('/ask', json=test_question)
        assert response.status_code == 400  # Expecting a bad request status if no answer can be retrieved
        assert 'error' in response.get_json()
        assert response.get_json()['error'] == 'Could not retrieve answer'
