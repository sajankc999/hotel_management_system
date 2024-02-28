from rest_framework.serializers import Serializer,ModelSerializer
from rest_framework import serializers
from .models import *
from Bookings.serializer import ReservationSerializer

class InvoiceSerializer(ModelSerializer):
    room_charge = serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = "__all__"
