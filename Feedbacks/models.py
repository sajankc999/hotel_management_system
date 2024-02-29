from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator
user_obj = get_user_model()
# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(user_obj, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    date = models.DateField(auto_now_add=True)
