import json

from tests.BaseCase import BaseCase


class SignupTest(BaseCase):

    def test_successful_signup(self):
        payload = json.dumps({
            "email": "sinaniya@gmail.com",
            "password": "my_password"
        })

        response = self.app.post(
            '/api/auth/signup',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
