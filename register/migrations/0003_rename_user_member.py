# Generated by Django 4.0.2 on 2022-04-18 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_rename_fname_user_username_remove_user_lname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Member',
        ),
    ]