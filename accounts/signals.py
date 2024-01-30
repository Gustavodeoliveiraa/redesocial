from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from social_network.models import ProfilePersonal


@receiver(post_save, sender=User)
def save_profile_personal_post_save_user(sender, instance, **kwargs):
    ProfilePersonal.objects.create(user=instance.username)
    print('apos validar o RegisterUser o User foi criado')
