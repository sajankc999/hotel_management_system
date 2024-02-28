
from Rooms.models import *
from django.contrib.auth import get_user_model
# Create your models here.
user_obj = get_user_model()
class guest(models.Model):
    # user = models.ForeignKey(user_obj,on_delete = models.CASCADE)
    full_name=models.CharField(max_length=300)
    email= models.EmailField()
    contact=models.CharField(max_length = 10)
    address=models.CharField(max_length=300)
  
    
class guest_room(models.Model):
    guest=models.ForeignKey(guest,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)