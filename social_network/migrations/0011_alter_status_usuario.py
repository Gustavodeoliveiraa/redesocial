# Generated by Django 4.2.3 on 2023-10-08 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0010_remove_profilepersonal_amigos_alter_status_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_network.profilepersonal'),
        ),
    ]