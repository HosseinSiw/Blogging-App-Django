from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
import pytest


@pytest.mark.django_db
class TestAuthenticationViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpass123'
        self.email = 'test@test.com'

    def create_test_user(self):
        return User.objects.create_user(username=self.username, email=self.email, password=self.password)

    def test_signup_view_get(self):
        """Test that signup view returns a 200 status code for GET request."""
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_post_success(self):
        """Test that signup view creates a new user upon successful registration."""
        self.create_test_user()  # Ensure user doesn't exist yet
        response = self.client.post(reverse('users:signup'), {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password1': 'newpass123',
            'password2': 'newpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(User.objects.filter(username='newuser').exists())
        messages = get_messages(response.wsgi_request)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Account created for newuser!')

    def test_signup_view_post_failure(self):
        """Test that signup view shows error messages for invalid inputs."""
        response = self.client.post(reverse('users:signup'), {
            'username': 'existinguser',
            'email': 'existinguser@test.com',
            'password1': 'short',
            'password2': 'short'
        })
        self.assertEqual(response.status_code, 200)
        messages = get_messages(response.wsgi_request)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Please correct the error below.')

    def test_login_view_get(self):
        """Test that login view returns a 200 status code for GET request."""
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_post_success(self):
        """Test that login view logs in a user upon successful credentials."""
        self.create_test_user()
        response = self.client.post(reverse('users:login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(response.url.endswith('/home/home'))  # Adjust according to your URL configuration

    def test_login_view_post_failure(self):
        """Test that login view shows error message for failed login attempt."""
        self.create_test_user()
        response = self.client.post(reverse('users:login'), {
            'username': 'wrong',
            'password': 'wrong'
        })
        self.assertEqual(response.status_code, 200)
        messages = get_messages(response.wsgi_request)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Invalid username or password.')

    def test_logout_view(self):
        """Test that logout view logs out a user and redirects to home page."""
        self.create_test_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(response.url.endswith('/home/home'))  # Adjust according to your URL configuration
