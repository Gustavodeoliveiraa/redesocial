from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('', views.Home.as_view(), name='account'),
    path('validate/', views.CreateUser.as_view(), name='create'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('process/form/', views.ProcessModelForm.as_view(), name='form'),

]
