from rest_framework import serializers
from .models import *
from Rooms.serializer import RoomSerializer
from .utils import send_confrimation_mail
from rest_framework.authtoken.models import Token
from datetime import datetime,timedelta
class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    room = RoomSerializer(read_only = True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset =Room.objects.all(),
        source = 'room'
    )
    class Meta:
        model = Reservation
        fields = ['user','room_id','room','check_in_date','check_out_date']
        # exclude  = ['status','confirmation_token']
    def validate(self, attrs):
        check_in = attrs.get('check_in_date')
        if datetime.now() > check_in:
            raise serializers.ValidationError('check-in date must be greater than today ')
        if datetime.now() > attrs.get('check_out_date'):
            raise serializers.ValidationError('check-out date must be greater than todays date')
        return super().validate(attrs)

class CancelReservationSerializer(serializers.ModelSerializer):
    
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = Reservation
        fields = ['id','user']

    def update(self, instance, validated_data):
        # raise Exception(instance)
        instance.status = 'canceled'
        instance.save()
        Room.objects.filter(id = instance.room.pk).update(status = 'V')
        return super().update(instance, validated_data)