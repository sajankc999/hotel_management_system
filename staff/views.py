from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .permission import *
from rest_framework.response import Response
class Staffview(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAdminUser,)

    
class Taskview(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminUser,)

    # def get_queryset(self):
    #     if self.request.user.is_admin:
    #         return Task.objects.all()
    #     if self.request.user.is_authenticated:
    #         return Task.objects.filter(user = self.request.user)

class ShiftView(ModelViewSet):
    queryset = ShiftSerializer
    serializer_class = StaffSerializer   
    permission_classes = (IsAdminUser,)