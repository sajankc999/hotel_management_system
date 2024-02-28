from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser
# Create your models here.
# user_obj = get_user_model()

class Shift(models.Model):
    shifts = (
        ('day','Day'),
        ('night','Night')
    )
    shift = models.CharField(max_length = 5 , choices = shifts)
    start_time = models.TimeField()
    end_time = models.TimeField()
class Staff(models.Model):
    full_name = models.CharField(max_length = 100)
    email = models.EmailField()
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True)
    Roles = (
        ('house_keeping','House Keeping'),
        ('front_desk','Front Desk'),
        ('management','Management'),
        ('security','Security'),
        
    )
    Role = models.CharField(max_length = 50 ,choices = Roles )

class Task(models.Model):
    staff = models.OneToOneField(Staff,on_delete= models.CASCADE)
    task_details = models.TextField()
    is_complete = models.BooleanField(default = False)
