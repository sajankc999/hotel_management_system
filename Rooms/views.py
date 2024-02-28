from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
# Create your views here.
from .models import *
from rest_framework.viewsets import generics, ModelViewSet
from .serializer import *
class RoomTypeView(ModelViewSet):
    queryset = Room_type.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = (IsAdminUser)

class RoomSerializer(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer