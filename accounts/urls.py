from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('', views.Home.as_view(), name='account'),
    path('validate/', views.CreateUser.as_view(), name='create'),
    path('login/', views.login_user, name='login'),
    path('process/form/', views.process_modal_form, name='form'),
   
]
