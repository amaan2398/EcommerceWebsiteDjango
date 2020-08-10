from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to = 'pics')
    description = models.TextField(blank=False,null=False)
    price = models.DecimalField(decimal_places=2,max_digits= 1000)
