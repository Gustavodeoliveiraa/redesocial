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

    usuario = models.ForeignKey(
        ProfilePersonal, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.status_image)


class Friends(models.Model):
    friend = models.ForeignKey(
        ProfilePersonal, on_delete=models.CASCADE, blank=True,
        related_name='reverse_friend'
    )

    user_reference = models.ForeignKey(
        ProfilePersonal, on_delete=models.CASCADE, blank=True
    )

    def __str__(self) -> str:
        return f"{str(self.friend)} is a friend of {self.user_reference}"


class Post(models.Model):
    user = models.ForeignKey(
        ProfilePersonal, on_delete=models.CASCADE, blank=False
    )
    text_post = models.TextField(max_length=300)
    public = models.CharField(max_length=10, null=True)

    def __str__(self) -> str:
        return f"Post of {str(self.user)}"


class ProfilePersonalModel(forms.ModelForm):
    class Meta:
        model = ProfilePersonal
        fields = ['profile_image']


class StatusModel(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status_image']
