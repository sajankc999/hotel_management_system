from django.db import models
from django.contrib.auth import get_user_model
from Rooms.models import Room
from django.utils import timezone
import uuid  # for generating unique tokens

# Create your models here.
user = get_user_model()
class Reservation(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField(default = timezone.now)
    check_out_date = models.DateField()
    status = models.CharField(max_length=20, default='inactive',choices = (('active','Active'),('inactive','Inactive'),('canceled','Cancled')))
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)  # Unique token for confirmation
