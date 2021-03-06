# Generated by Django 4.0.2 on 2022-05-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobVacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='date_added',
        ),
    ]
