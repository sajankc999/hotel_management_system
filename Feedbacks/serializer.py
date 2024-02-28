from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import *

class FeedbackSerializer(ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = Feedback
        fields = "__all__"