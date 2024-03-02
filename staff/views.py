from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet,generics
from .models import *
from .serializer import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .permission import *
from rest_framework.response import Response
class Staffview(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    # permission_classes = (IsAdminUser,IsAuthenticated)
    permission_classes=(IsAuthenticated,)


    def get_queryset(self):
        # if self.request.user.is_superuser and self.request.user.is_staff:
        #     return Staff.objects.all()
        if self.request.user.is_staff:
            return Staff.objects.filter(user = self.request.user)
        
        
    # def post(self,request,*args, **kwargs):
    #     if  self.request.user.is_superuser:
    #         self.create(request,*args, **kwargs)
    #     else:
    #         return Response('only superuser can create staff records')
    
class Staffadminview(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    # permission_classes = (IsAdminUser,IsAuthenticated)
    permission_classes=(IsAdminUser,)


class Taskview(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # if self.request.user.is_superuser and self.request.user.is_staff:
        #     return Task.objects.all()
        if self.request.user.is_authenticated:
            staff= Staff.objects.filter(user = self.request.user).first()
            # raise Exception(staff)
            if staff:
                return Task.objects.filter(staff=staff)
        
class Taskadminview(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminUser,)

    # def get(self,request,*args, **kwargs):
    #     # if self.request.user.is_superuser and self.request.user.is_staff:
    #     #     return Task.objects.all()
    #     if self.request.user.is_authenticated:
    #         return Task.objects.filter(user = self.request.user)
    #     return Response('invalid credentials')
       

class ShiftView(ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer   
    permission_classes = (IsAdminUser,)