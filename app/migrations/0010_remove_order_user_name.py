# Generated by Django 4.2 on 2023-05-29 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_name',
        ),
    ]
