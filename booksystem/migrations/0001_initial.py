# Generated by Django 2.2.6 on 2019-10-29 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_items', models.IntegerField()),
                ('cashier', models.CharField(default='Common', max_length=100)),
                ('list_of_items', models.CharField(max_length=10000)),
                ('billed_at', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField(default=200)),
            ],
            options={
                'get_latest_by': 'billed_at',
            },
        ),
        migrations.CreateModel(
            name='Book_Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_decription', models.TextField(max_length=50000)),
                ('no_items', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book_System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_publisher_name', models.CharField(max_length=500)),
                ('receipt_publisher_address', models.CharField(max_length=800)),
                ('receipt_greenting_text', models.CharField(max_length=800)),
                ('receipt_date', models.BooleanField(default=True)),
                ('receipt_no_items', models.BooleanField(default=True)),
                ('receipt_subtotal', models.BooleanField(default=True)),
                ('receipt_total', models.BooleanField(default=True)),
                ('signal_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Signal_User_Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=500)),
                ('book_price', models.IntegerField()),
                ('item_code', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksystem.Author')),
                ('book_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksystem.Book_Type')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksystem.Book_Publisher')),
            ],
        ),
    ]
