from django.db import models

# Create your models here.
class Cart(models.Model):
    customer_id = models.IntegerField(blank=False,null=False)
    product_id = models.IntegerField(blank=False,null=False)
    product_quantity = models.IntegerField(blank=False,null=False)
    shipment = models.BooleanField(blank=False,null=False,default=False)
    