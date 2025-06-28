from django.db import models

class Categories(models.TextChoices):
  FITNESS = 'Fitness'
  ELECTRONICS = 'Electronics'
  FURNITURE = 'Furniture'
  KITCHEN = 'Kitchen'
  CLOTHING = 'Clothing'
  ACCESSORIES = 'Accessories'
  

class Product(models.Model):
  title = models.CharField(max_length=35);
  price = models.FloatField();
  description = models.TextField();
  category = models.CharField(max_length=20,choices=Categories.choices);
  image = models.URLField();
  sold = models.BooleanField();
  isSale = models.BooleanField();
  dateOfSale = models.DateField(null=True)
# Create your models here.
