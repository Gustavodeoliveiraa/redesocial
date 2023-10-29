# Generated by Django 4.2.3 on 2023-10-06 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_network', '0006_remove_profilepersonal_friend_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepersonal',
            name='friend_user',
        ),
        migrations.AddField(
            model_name='profilepersonal',
            name='friend_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]