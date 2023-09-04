from django.test import TestCase
from django.urls import reverse
from accounts.models import User


class TestViewCreateUser(TestCase):
    def test_view_register_with_success(self):
        data = {
            'username': 'User',
            'email': 'email@email.com',
            'password': 'SenhaTeste123',
            'password2': 'SenhaTeste123'
        }
        response = self.client.post(
            reverse('accounts:create'), data=data, follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('accounts:account'))
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTrue(User.objects.filter(username='User').exists())
        self.assertContains(response, 'account created with success')

    def test_view_register_unsuccessfully_and_empty_password_or_username(self):
        User.objects.create(
            username='User', email='email@email.com',
            password='SenhaTeste123',
        )

        data = {
            'username': '',
            'email': 'email@email.com',
            'password': '',
            'password2': ''
        }

        response = self.client.post(
            reverse('accounts:create'), data=data, follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'username', ['This field not be empty']
        )

        self.assertFormError(
            response, 'form', 'email', ['This email is already in use']
        )

        self.assertFormError(
            response, 'form', 'password', ['This field not must by empty'])

        self.assertFormError(
            response, 'form', 'password2', ['This field is required.'])

    def test_view_register_unsuccessfully_weak_and_different_password(self):
        data = {
            'username': 'User',
            'email': 'email@email.com',
            'password': '123',
            'password2': '1234'
        }

        response = self.client.post(
            reverse('accounts:create'), data=data, follow=True
        )

        self.assertFormError(
            response, 'form', 'password',
            ['Password must contain at least 1 lowercase letter1 uppercase letter, 1 number and 8 or more characters'] # noqa
        )

        self.assertFormError(
            response, 'form', 'password2', ['passwords must be the same'])
