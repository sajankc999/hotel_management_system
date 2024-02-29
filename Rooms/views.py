from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
# Create your views here.
from .models import *
from rest_framework.viewsets import generics, ModelViewSet
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoomFilter
class RoomTypeView(ModelViewSet):
    queryset = Room_type.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = (IsAdminUser,)

class Roomview(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter