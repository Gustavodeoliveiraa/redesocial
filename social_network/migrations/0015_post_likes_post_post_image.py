# Generated by Django 4.0 on 2023-11-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0014_alter_post_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='social_network/covers/post'),
        ),
    ]
