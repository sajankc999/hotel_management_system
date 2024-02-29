from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator



# Create your models here.
class Room_type(models.Model):
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

    def __str__(self):
        return self.name
    
    


class Room(models.Model):
    # room_no=models.SmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(99)])
    room_no=models.SmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    floor=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    description=models.CharField(max_length=300)
    bed_count=models.IntegerField()
    room_status=[('V','Vacant'),('R','Reserved'),('P','Pending'),('B','Booked'),('na','Not Available')]
    status=models.CharField(max_length=2,choices=room_status,default = 'V')
    type=models.ForeignKey(Room_type,on_delete=models.SET_NULL,null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self) -> str:
    #     return str(self.floor)+str(self.room_no) 