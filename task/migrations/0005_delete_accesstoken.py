# Generated by Django 4.1.7 on 2023-03-29 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_user_accesstoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccessToken',
        ),
    ]
