# Generated by Django 2.2.6 on 2019-10-30 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal_user_profile',
            name='user_linked',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signal_user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
