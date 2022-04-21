from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self):
        return self.name


class SneakerForMan(models.Model):
    sneaker_name=models.CharField(max_length=50)
    sneaker_model=models.CharField(max_length=50)
    sneaker_image=models.ImageField(null=True, blank=True, upload_to="imagesman/")
    size_choice = (
                ('40','40'),
                ('41','41'),
                ('42','42'),
                ('43','43'),
                ('44','44'),
                ('45','45'),
    )
    sneaker_size=models.CharField(max_length=2, blank=True, null=True, choices=size_choice)
    sneaker_price=models.IntegerField(null=True)
    sneaker_category=models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.sneaker_name + " " + self.sneaker_model



class SneakerForWoman(models.Model):
    sneaker_name=models.CharField(max_length=50)
    sneaker_model=models.CharField(max_length=50)
    sneaker_image=models.ImageField(null=True, blank=True, upload_to="imageswoman/")
    size_choice = (
                ('35','35'),
                ('36','36'),
                ('37','37'),
                ('38','38'),
                ('39','39'),
    )
    sneaker_size=models.CharField(max_length=2, blank=True, null=True, choices=size_choice)
    sneaker_price=models.IntegerField(null=True)
    sneaker_category=models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.sneaker_name + " " + self.sneaker_model


class SneakerForKid(models.Model):
    sneaker_name=models.CharField(max_length=50)
    sneaker_model=models.CharField(max_length=50)
    sneaker_image=models.ImageField(null=True, blank=True, upload_to="imageskid/")
    size_choice = (
                ('28','28'),
                ('29','29'),
                ('30','30'),
                ('31','31'),
                ('32','32'),
                ('33','33'),
                ('34','34'),
    )
    sneaker_size=models.CharField(max_length=2, blank=True, null=True, choices=size_choice)
    sneaker_price=models.IntegerField(null=True)
    sneaker_category=models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.sneaker_name + " " + self.sneaker_model

class ProductCategories(models.Model):
    category_choice = (
        ('Run','Run'),
        ('Volleyball','Volleyball'),
        ('Outerwear','Outerwear'),
        ('Collaborations','Collaborations'),
    )
    sneaker_category = models.CharField(max_length=30, blank=True, null=True, choices=category_choice)