# Generated by Django 4.0.2 on 2022-04-30 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_category_product_image_product_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
    ]