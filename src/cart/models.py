from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Cart(models.Model):
    customer_id = models.IntegerField(blank=False,null=False)
    product_id = models.IntegerField(blank=False,null=False)
    address_id = models.IntegerField(blank=False,null=False,default=0)
    bill_id = models.IntegerField(blank=False,null=False,default=0)
    product_quantity = models.IntegerField(blank=False,null=False)
    shipment = models.BooleanField(blank=False,null=False,default=False)

class Shipment(models.Model):
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    customer_id = models.IntegerField(blank=False,null=False)
    total_amount = models.IntegerField(blank=False,null=False)
