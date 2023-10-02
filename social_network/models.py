from django.db import models
from django import forms
from django.contrib.auth.models import User


class ProfilePersonal(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, related_name='my_profile'
    )

    profile_image = models.ImageField(
        upload_to='social_network/covers/profile/', blank=True, default=None
    )

    def __str__(self) -> str:
        return str(self.user)


class Status(models.Model):
    status_image = models.ImageField(
        upload_to='social_network/covers/status', blank=True
    )

    usuario = models.ForeignKey(ProfilePersonal, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.status_image)


class ProfilePersonalModel(forms.ModelForm):
    class Meta:
        model = ProfilePersonal
        fields = ['profile_image']


class StatusModel(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status_image']