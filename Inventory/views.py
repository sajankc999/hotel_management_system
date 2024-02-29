from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
from rest_framework.permissions import IsAdminUser
from .permission import *
# Create your views here.
from .models import *
from .serializer import *
class Supplierview(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsManager,)
class InvetoryItemview(ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = (IsManager,)

