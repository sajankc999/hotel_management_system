from django.db import models




# Create your models here.
class Room_type(models.Model):
    name=models.CharField(max_length=300)
    room_types = (
        ('S','standard'),
        ('D','Deluxe'),
        ('SU','suite'),
        ('DD','Double Deluxe'),
    )
    name = models.CharField(max_length=2,choices = room_types,default = 'S')
    amenities = models.TextField()
    room_charge = models.DecimalField(max_digits=10, decimal_places=2)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField()
    


class Room(models.Model):
    room_no=models.CharField(max_length=300)
    floor=models.CharField(max_length=300)
    description=models.CharField(max_length=300)
    bed_count=models.IntegerField()
    room_status=[('V','Vacant'),('R','Reserved'),('P','Pending'),('B','Booked')]
    status=models.CharField(max_length=1,choices=room_status,default = 'V')
    type=models.ForeignKey(Room_type,on_delete=models.SET_NULL,null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)