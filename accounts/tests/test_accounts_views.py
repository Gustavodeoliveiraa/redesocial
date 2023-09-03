from django.test import TestCase
from django.urls import reverse, resolve
from accounts import views


class AccountsViewsTest(TestCase):
    def test_home_function_view_is_correct(self):
        view_entry = resolve(reverse('accounts:account'))
        self.assertIs(views.entry, view_entry.func)

    def test_validade_function_view_is_correct(self):
        view_validate = resolve(reverse('accounts:create'))
        self.assertIs(views.create_user, view_validate.func)

    def test_login_function_view_is_correct(self):
        view_login = resolve(reverse('accounts:login'))
        self.assertIs(views.login_user, view_login.func)

    def test_process_form_function_view_is_correct(self):
        view_process = resolve(reverse('accounts:form'))
        self.assertIn(views.process_modal_form, view_process)