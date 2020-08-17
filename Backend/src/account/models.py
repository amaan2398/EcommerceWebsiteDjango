from django.db import models

# Create your models here.
class Address(models.Model):
    customer_id = models.IntegerField(blank=False,null=False)
    street_address = models.CharField(max_length=125)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    postcode = models.CharField(max_length=10)