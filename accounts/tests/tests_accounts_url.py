from django.test import TestCase
from django.urls import reverse


class AccountsUrlsTest(TestCase):
    def test_home_url_is_correct(self):
        self.assertEqual(reverse('accounts:account'), '/')

    def test_validade_url_is_correct(self):
        self.assertEqual(reverse('accounts:create'), '/validate/')

    def test_login_url_is_correct(self):
        self.assertEqual(reverse('accounts:login'), '/login/')

    def test_process_form_url_is_correct(self):
        self.assertEqual(reverse('accounts:form'), '/process/form/')
