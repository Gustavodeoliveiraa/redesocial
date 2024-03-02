from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from social_network.models import ProfilePersonal


@receiver(post_save, sender=User)
def save_profile_personal_post_save_user(sender, instance, created, **kwargs):
    # After creating a user, register this user in the ProfilePersonal.
    if created:
        ProfilePersonal.objects.create(user=instance)
