# Generated by Django 2.2.6 on 2019-10-31 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booksystem', '0013_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='owner_book_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booksystem.Book_System'),
        ),
    ]