# Generated by Django 4.0.2 on 2022-04-21 09:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_sneaker_sneaker_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='sneaker_size',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None),
        ),
    ]
