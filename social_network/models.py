from django.db import models
from django import forms
from django.contrib.auth.models import User


class Comments(models.Model):
    username = models.TextField(max_length=100, blank=True)
    comments = models.TextField(max_length=150, blank=True)


class Publication(models.Model):
    publication_image = models.ImageField(
        upload_to='social_network/covers/publication', blank=True
    )
    publication_description = models.TextField(max_length=150,  blank=True)
    likes = models.IntegerField(blank=True)
    comments = models.ForeignKey(
        Comments, on_delete=models.CASCADE, blank=True
    )


class Status(models.Model):
    status_image = models.ImageField(
        upload_to='social_network/covers/publication', blank=True
    )
    status_video = models.FileField(
        upload_to='social_network/covers/status/video', blank=True
    )


class ProfilePersonal(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, related_name='my_profile'
    )
    publication = models.ForeignKey(
        Publication, on_delete=models.CASCADE, blank=True, null=True
    )
    friends = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name='my_friends',
        null=True
    )
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)

    profile_image = models.ImageField(
        upload_to='social_network/covers/profile/', blank=True, default=None
    )

    def __str__(self) -> str:
        return str(self.user)


class ProfilePersonalModel(forms.ModelForm):
    class Meta:
        model = ProfilePersonal
        fields = ['profile_image']


class StatusModel(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status_video']