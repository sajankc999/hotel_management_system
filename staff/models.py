from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
# from django.contrib.auth.models import AbstractUser
# Create your models here.
user_obj = get_user_model()

class Shift(models.Model):
    shifts = (
        ('day','Day'),
        ('night','Night')
    )
    shift = models.CharField(max_length = 5 , choices = shifts)
    start_time = models.TimeField()
    end_time = models.TimeField()
class Staff(models.Model):
    user = models.OneToOneField(user_obj,on_delete = models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True)
    # Roles = (
    #     ('house_keeping','House Keeping'),
    #     ('front_desk','Front Desk'),
    #     ('management','Management'),
    #     ('security','Security'),
        
    # )
    # Role = models.CharField(max_length = 50 ,choices = Roles )

class Task(models.Model):
    staff = models.OneToOneField(Staff,on_delete= models.CASCADE)
    task_details = models.TextField()
    is_complete = models.BooleanField(default = False)

@receiver(post_save, sender=Task)
def TaskSaved(sender, instance,*args,**kwargs):
    send_mail(
        "Task for you",
        "hello employee, we have a task for you .please complete your task and report to your supervisor",
        "falanahotel@mail.mail",
        [instance.staff.user.email],
    )
    

