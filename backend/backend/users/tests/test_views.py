from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from backend.users.tests.factories import UserFactory
from backend.users.models import User


class TestSignUpUser(TestCase):
    def setUp(self):
        self.url = reverse('users:signup')
        self.client = APIClient()
        self.request_body = {
            'first_name': 'Seb',
            'last_name': 'Ozi',
            'email': "s@gmail.com",
            'password': 'StrongPassword444@',
            'agree_with_terms': True,
        }

    def test_signup_successfully(self):
        response_body = {
            'first_name': 'Seb',
            'last_name': 'Ozi',
            'email': "s@gmail.com",
        }
        response = self.client.post(self.url, self.request_body)

        self.assertEqual(response.data, response_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.get(email=self.request_body['email']))

    def test_signup_user_that_already_exists(self):
        UserFactory.create(email=self.request_body['email'])
        response_body = {'email': ['user with this email address already exists.']}
        response = self.client.post(self.url, self.request_body)

        self.assertEqual(response.data, response_body)
        self.assertTrue(User.objects.get(email=self.request_body['email']))


class TestSignInUser(TestCase):
    def setUp(self):
        self.user = UserFactory.create(email='s@gmail.com', password='StrongPassword444@')

        self.url = reverse('users:signin')
        self.client = APIClient()
        self.request_body = {'email': self.user.email, 'password': 'StrongPassword444@'}

    def test_signin_successfully(self):
        response = self.client.post(self.url, self.request_body)

        cookies = response.client.cookies
        self.assertIn('HttpOnly', str(cookies.get('csrftoken')))
        self.assertIn('HttpOnly', str(cookies.get('sessionid')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_user_with_invalid_credentials(self):
        self.request_body['password'] = 'seb4@gmai.com'
        response_body = {"detail": "Invalid credentials"}
        response = self.client.post(self.url, self.request_body)

        self.assertEqual(response.data, response_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestGetCurrentUserData(TestCase):
    def setUp(self):
        self.user = UserFactory.create(email='s@gmail.com', password='StrongPassword444@')

        self.url = reverse('users:current-user')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_get_user_data_successfully(self):
        request_body = {"first_name": self.user.first_name, "last_name": self.user.last_name, "email": self.user.email}

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, request_body)
