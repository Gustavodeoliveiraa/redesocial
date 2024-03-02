from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from social_network.models import User
from social_network.views import feed
# from django.core.files.uploadededfile import SimpleUploadededFile


class TestViewFeed(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create(
            username="Teste02", password="Testesenha01"
        )
        self.request_for_view_feed = self.factory.get('/feed/')
        self.request_for_view_feed.user = self.user
        return super().setUp()

    def test_feed_view_returns_200_status_code(self):
        request = self.request_for_view_feed
        response = feed(request)
        self.assertEqual(response.status_code, 200)

    def test_feed_view_redirects_unauthenticated_user(self):
        request = self.request_for_view_feed
        request.user = AnonymousUser()
        response = feed(request)
        self.assertEqual(response.status_code, 302)

    def test_if_user_is_loaded_correctly(self):
        request = self.request_for_view_feed
        self.assertEqual(request.user.get_username(), 'Teste02')

    def test_if_profile_image_default_is_loaded_correctly(self):
        request = self.request_for_view_feed
        path_image = '/static/img/without_user.png'

        response = feed(request)
        render_html = response.content.decode('utf8')
        self.assertIn(path_image, render_html)

    def test_if_form_for_change_profile_image_is_loaded_correctly(self):
        request = self.request_for_view_feed
        response = feed(request)

        self.assertIn(
            '<form action=" /process_image/', response.content.decode('utf8')
        )
        self.assertIn('name="profile_image" ', response.content.decode('utf8'))