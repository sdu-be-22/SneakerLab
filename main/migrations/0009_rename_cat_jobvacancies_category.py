# Generated by Django 4.0.2 on 2022-05-22 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_jobvacancies_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobvacancies',
            old_name='cat',
            new_name='category',
        ),
    ]
