from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import CustomPasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('social_network.urls')),

    path(
        'reset-password/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),

    path(
        'reset-password/done/', 
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset-password/<uidb64>/<token>/', 
        CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    path(
        'reset-password/complete/', 
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += path("__debug__/", include("debug_toolbar.urls")),