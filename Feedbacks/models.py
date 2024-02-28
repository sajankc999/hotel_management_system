from django.db import models
from django.contrib.auth import get_user_model
user_obj = get_user_model()
# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(user_obj, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)
