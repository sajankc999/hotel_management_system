from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import IsAdminUser

class Staffview(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAdminUser,)

class Taskview(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminUser,)

class ShiftView(ModelViewSet):
    queryset = ShiftSerializer
    serializer_class = StaffSerializer
    permission_classes = (IsAdminUser,)