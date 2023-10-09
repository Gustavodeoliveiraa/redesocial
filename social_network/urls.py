from django.urls import path
from social_network import views

urlpatterns = [
    path("feed/", views.feed, name="feed"),
    path("process_image/", views.process_image, name="process_image"),
    path("logout/", views.logout_view, name="logout"),
    path("create_status/", views.create_status, name="create_status"),
    path("status/<str:user>", views.show_status_of_a_user, name='all_status'),
    path("feed/search_user/<str:user>", views.search_users, name='search_users')
]
