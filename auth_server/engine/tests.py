from django.test import TestCase
from engine.models import User
from rest_framework.test import APIRequestFactory, APIClient
import json

# Create your tests here.


class EngineTests(TestCase):

    factory = APIRequestFactory()
    client = APIClient()
    REQUESTS = {
        'GenerateTokensView': {
            'route': 'http://127.0.0.1:8000/tokens/login/',
            'tests': [
                {
                    'body': {'email': 'testuser@gmail.com', 'password': 'password'},
                    'assert': 200
                },
                {
                    'body': {'email': 'userthatdoesnotexist@gmail.com', 'password': 'password'},
                    'assert': 400
                },
                {
                    'body': {'email': 'testuser@gmail.com'},
                    'assert': 400
                }
            ]
        }
    }

    def test_GenerateTokensView(self):
        """Tests for the token login view"""

        # Creating the default user
        User.objects.create_user(
            email='testuser@gmail.com', password='password')

        # Executing all the requests
        for x in self.REQUESTS['GenerateTokensView']['tests']:
            request = self.client.post(
                self.REQUESTS['GenerateTokensView']['route'],
                json.dumps(x['body']),
                content_type='application/json'
            )
            assert request.status_code == x['assert']
