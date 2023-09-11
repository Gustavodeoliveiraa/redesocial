from django.urls import path
from social_network import views

urlpatterns = [
    path("feed/", views.t, name="feed")
]
