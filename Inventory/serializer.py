from rest_framework.serializers import Serializer
from .models import *

class SupplierSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__al__"

class InventoryItemSerializer(Serializer.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = "__all__"

