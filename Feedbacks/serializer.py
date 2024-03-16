from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import *
from django.contrib.auth import get_user_model

user_obj= get_user_model()
class FeedbackSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_info = serializers.SerializerMethodField()
    class Meta:
        model = Feedback
        fields = "__all__"
    
    def get_user_info(self,feedback):
        return feedback.user.email