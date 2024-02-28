from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length = 50,choices =(('toiletries','toiletries'),('linens','linens'),('supplies','supplies')),default ='toiletries')
    reorder_level = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

@receiver(post_save, sender=InventoryItem)
def send_reorder_email(sender, instance, created, **kwargs):
    
    if not created:  # Check if the Inventory instance is being updated
        if instance.quantity <= instance.reorder_level:
            # print(instance.supplier.email)
            send_mail(
                "Requesting for fulfillment of shortage in item",
                f" dear supplier {instance.supplier.name} , product id:{instance.pk},name :{instance.name} is running out of stock . we need you to provide another batch of stock",
                "falanahotel@hh.com",
                [instance.supplier.email,]
            )