from django.db import models

# Create your models here.


class ProfilePersonal(models.Model):
    user_image = models.ImageField(
        upload_to='social_network/covers/', blank=True
    )

    profile_image = models.ImageField(
        upload_to='social_network/covers/profile/', blank=True
    )

    def __str__(self) -> str:
        return self.__class__.__name__
