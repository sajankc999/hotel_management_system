from rest_framework.serializers import Serializer,ModelSerializer
from rest_framework import serializers
from .models import *
from Bookings.serializer import ReservationSerializer

class InvoiceSerializer(ModelSerializer):
    reservation = ReservationSerializer()
    class Meta:
        model = Invoice
        fields = "__all__"
