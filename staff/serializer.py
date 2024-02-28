from rest_framework import serializers
from .models import *
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model =Shift
        fields = "__all__"
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields= ['staff','task_details']

class StaffSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer(read_only = True)
    class Meta:
        model = Staff
        fields = "__all__"