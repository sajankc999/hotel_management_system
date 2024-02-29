from rest_framework import serializers
from .models import *
from authUser.serializers import UserSerializer
from django.contrib.auth import get_user_model
user_obj = get_user_model()
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model =Shift
        fields = "__all__"
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields= "__all__"

class StaffSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    user = serializers.StringRelatedField()
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = user_obj.objects.all(),
        source ='user'
    )
    shift = ShiftSerializer(read_only = True)
    shift_id = serializers.PrimaryKeyRelatedField(
        queryset = Shift.objects.all(),
        source ='shift'
    )
    class Meta:
        model = Staff
        fields = "__all__"