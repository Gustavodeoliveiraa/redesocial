from django.urls import path
from social_network import views

urlpatterns = [
    path("feed/", views.feed, name="feed"),
    path("process_image/", views.process_image, name="process_image"),
    path("logout/", views.logout_view, name="logout"),
    path("create_status/", views.create_status, name="create_status"),
    path("status/<str:user>", views.show_status_of_a_user, name='all_status'),
    path(
        "feed/search_user/<str:user>", views.search_users, name='search_users'
    ),
    path("feed/add/notify/<str:user>", views.send_notify_add_friend, name='notify'),
    path("feed/add/<str:user>/<int:notify_id>/", views.add_friends, name='add_friends'),

    path(
        "feed/add/delete/post/<str:pk>", views.delete_post, name='delete_post'
    ),

    path("feed/add/new/post", views.add_post, name='add_post'),

    path(
        "feed/counter/likes/<int:post_id>/<int:likes>",
        views.num_likes_of_post,
        name='counter_Likes'
    ),

    path(
        "feed/delete/friend/<str:pk>",
        views.delete_friend,
        name='delete_friend'
    ),

]
