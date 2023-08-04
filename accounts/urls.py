from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('', views.entry, name='account'),
    path('validate/', views.create_user, name='create'),
    path('login/', views.login_user, name='login'),
    path('login/change-password/', views.change_password, name='password'),
]