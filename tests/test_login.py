import json

from tests.BaseCase import BaseCase


class TestUserLogin(BaseCase):

    def test_successful_login(self):
        payload = json.dumps({
            "email": "sinaniya@gmail.com",
            "password": "my_password"
        })

        response = self.app.post(
            '/api/auth/signup',
            headers={"Content-Type": "application/json"},
            data=payload)

        response = self.app.post(
            '/api/auth/login',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)
