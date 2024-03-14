# Generated by Django 4.2.3 on 2024-03-13 03:55

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0017_alter_post_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='Valor Padrão', max_length=255)),
                ('read', models.BooleanField(default=False)),
                ('verb', models.CharField(blank=True, max_length=255, null=True)),
                ('recipient_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='received_notifications', to='social_network.profilepersonal')),
            ],
            managers=[
                ('unread', django.db.models.manager.Manager()),
            ],
        ),
    ]