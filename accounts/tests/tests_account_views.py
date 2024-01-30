from django.test import TestCase, RequestFactory
from django.urls import reverse
from accounts.models import User
from accounts.views import send_email_async
import os
from unittest.mock import patch
from django.core import mail
from social_network.models import ProfilePersonal


class TestViewCreateUser(TestCase):
    def test_view_register_with_success(self):
        data = {
            'username': 'User',
            'email': 'email@email.com',
            'password': 'SenhaTeste123',
            'password2': 'SenhaTeste123'
        }
        response = self.client.post(
            reverse('accounts:create'), data=data,
        )
        print(response.status_code)

        self.assertEqual(response.status_code, 200)
         
        self.assertFalse(response.context['user'].is_authenticated)
        # self.assertTrue(User.objects.filter(username='User').exists())
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


class TestViewLoginUser(TestCase):
    def test_login_user_authenticated(self):
        user = User.objects.create_user(  # type: ignore
            username='User',
            password='123'
        )
        ProfilePersonal.objects.create(user=user)

        data = {
            'username': 'User',
            'password': '123',
        }
        response = self.client.post(
            reverse('accounts:login'), follow=True, data=data
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_user_not_authenticated(self):
        User.objects.create_user(  # type: ignore
            username='User',
            password='1234'
        )

        data = {
            'username': 'User',
            'password': '123',
        }

        response = self.client.post(
            reverse('accounts:login'), follow=True, data=data
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertIn('Credentials invalid', response.content.decode('utf-8'))


class TestProcessModalForm(TestCase):
    def test_whether_email_will_be_send(self):
        User.objects.create_user(  # type: ignore
            username='User',
            email=os.environ.get('EMAIL')
        )

        request = RequestFactory().post(reverse('accounts:form'))

        with patch(
            'project.settings.EMAIL_BACKEND', 
                new='django.core.mail.backends.console.EmailBackend'):
            root_path = send_email_async(
                request, 'User', os.environ.get('EMAIL')
            )[0]
            email = mail.outbox[0]

            self.assertIn('redefinição de senha', email.subject)
            self.assertIn(root_path, email.body)
            self.assertIn(os.environ.get('EMAIL_HOST_USER'), email.from_email)
            self.assertIn(os.environ.get('EMAIL'), email.to)

    def test_logic_of_the_view_modal_form(self):
        User.objects.create_user(  # type: ignore
            username='User',
            email=os.environ.get('EMAIL')
        )

        data = {
            'username': 'User',
            'email': os.environ.get('EMAIL')
        }

        response = self.client.post(reverse('accounts:form'), data=data)
        self.assertIn('Email send', response.content.decode('utf-8'))

    def test_error_of_the_view_modal_form(self):
        response = self.client.post(reverse('accounts:form'))
        self.assertIn('Something is wrong', response.content.decode('utf-8'))
