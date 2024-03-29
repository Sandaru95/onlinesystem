# Generated by Django 2.2.6 on 2019-10-30 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booksystem', '0006_book_publisher_owner_book_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='owner_book_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booksystem.Book_System'),
        ),
        migrations.AddField(
            model_name='bill',
            name='owner_book_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booksystem.Book_System'),
        ),
        migrations.AddField(
            model_name='book_type',
            name='owner_book_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booksystem.Book_System'),
        ),
        migrations.AddField(
            model_name='cashier',
            name='owner_book_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booksystem.Book_System'),
        ),
    ]
