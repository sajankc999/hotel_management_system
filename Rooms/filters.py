from .models import *

from django_filters import FilterSet

class RoomFilter(FilterSet):
    class Meta:
        model=Room
        fields={
            'floor':['gte','lte'],
            'bed_count':['gte','lte'],
            'status':['exact'],
            'type':['exact'],
        }