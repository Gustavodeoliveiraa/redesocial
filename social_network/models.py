from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class ProfilePersonal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    user_image = models.ImageField(
        upload_to='social_network/covers/', blank=True, default=None
    )

    profile_image = models.ImageField(
        upload_to='social_network/covers/profile/', blank=True, default=None
    )

    def __str__(self) -> str:
        return str(self.user)


class ProfilePersonalModel(forms.ModelForm):
    class Meta:
        model = ProfilePersonal
        fields = ['user_image', 'profile_image']
