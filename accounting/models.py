from django.db import models

# Create your models here.
from Bookings.models import Reservation
from uuid import uuid4


class Invoice(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    special_discount = models.PositiveIntegerField()
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length = 50,choices = (('esewa','esewa'),('khalti','khalti'),("fhonepay",'fhonepay')),default = 'esewa')
    billing_date = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default = False)
    payment_id = models.UUIDField(default = uuid4 ,editable = False)