from django.test import TestCase
from django.urls import reverse, resolve
from accounts import views


class AccountsViewsTest(TestCase):

    # def test_home_function_view_is_correct(self):
    #     view_entry = resolve(reverse('accounts:account'))
    #     self.assertIs(views.home, view_entry.func)

    def test_home_class_view_is_correct(self):
        # test if class Home is loading correctly
        resolved_class = resolve(reverse('accounts:account'))
        self.assertIs(resolved_class.func.view_class, views.Home)

    def test_validade_function_view_is_correct(self):
        resolved_class = resolve(reverse('accounts:create'))
        self.assertIs(resolved_class.func.view_class, views.CreateUser)

    def test_login_function_view_is_correct(self):
        view_login = resolve(reverse('accounts:login'))
        self.assertIs(view_login.func.view_class, views.UserLogin)

    def test_process_form_function_view_is_correct(self):
        view_process = resolve(reverse('accounts:form'))
        self.assertIn(views.process_modal_form, view_process)
