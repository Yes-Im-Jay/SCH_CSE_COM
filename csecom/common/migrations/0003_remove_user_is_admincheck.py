# Generated by Django 4.2 on 2023-06-20 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_user_is_admincheck_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admincheck',
        ),
    ]