from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class TestTemplateContentAccountsLogin(TestCase):
    @parameterized.expand([
        ('enter your account'),
        ('or use your email account'),
        ('Username'),
        ('Password'),
        ('Create account'),
        ('enter your personal detail'),
        (' and start your journey with us'),
        ('Sign in'),
    ])
    def test_content_login_template(self, string_content):
        content = self.client.get(reverse('accounts:account'))
        self.assertIn(string_content, content.content.decode('utf-8'))


class TestTemplateContentAccountsRegister(TestCase):
    @parameterized.expand([
        ('or use your email for registration'),
        ('Username'),
        ('Email'),
        ('Password'),
        ('Confirm Password'),
        ('Sign up'),
        ('to connect with us'),
        ('please login with your personal info'),
    ])
    def test_content_register_template(self, string_content):
        content = self.client.get(reverse('accounts:account'))
        self.assertIn(string_content, content.content.decode('utf-8'))
