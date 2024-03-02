from django.test import TestCase
from django.urls import reverse


class SocialNetworkUrlTest(TestCase):
    def test_feed_url_is_correct(self):
        self.assertEqual(reverse('feed'), '/feed/')

    def test_process_image_url_is_correct(self):
        self.assertEqual(reverse('process_image'), '/process_image/')

    def test_logout_url_is_correct(self):
        self.assertEqual(reverse('logout'), '/logout/')

    def teste_create_status_user_is_correct(self):
        self.assertEqual(reverse('create_status'), '/create_status/')

    def teste_show_status_of_a_user_url_is_correct(self):
        self.assertEqual(reverse('all_status', args=(1,)), '/status/1')

    def test_search_users_url_is_correct(self):
        self.assertEqual(
            reverse('search_users', args=(1,)), '/feed/search_user/1'
        )

    def test_add_friends_url_is_correct(self):
        self.assertEqual(reverse('add_friends', args=(1,)), '/feed/add/1')

    def test_delete_post_url_is_correct(self):
        self.assertEqual(
            reverse('delete_post', args=(1,)),
            '/feed/add/delete/post/1'
        )

    def test_add_post_url_is_correct(self):
        self.assertEqual(reverse('add_post'), '/feed/add/new/post')

    def test_num_likes_of_post_url_is_correct(self):
        self.assertEqual(
            reverse('counter_Likes', args=(1, 2)),
            '/feed/counter/likes/1/2'
        )

    def test_delete_friend_url_is_correct(self):
        self.assertEqual(
            reverse('delete_post', args=(1,)), '/feed/add/delete/post/1'
        )
