from rest_framework import serializers
from .models import *
from Rooms.serializer import RoomSerializer
from .utils import send_confrimation_mail
from rest_framework.authtoken.models import Token
from django.utils import timezone
class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    room = RoomSerializer(read_only = True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset =Room.objects.all(),
        source = 'room'
    )
    check_in_date = serializers.DateField()
    check_out_date = serializers.DateField()
    class Meta:
        model = Reservation
        fields = ['user','room_id','room','check_in_date','check_out_date','status']
        # exclude  = ['status','confirmation_token']
    # def validate(self, attrs):
    #     check_in = attrs.get('check_in_date')  
    #     check_out = attrs.get('check_out_date')  

        # # if timezone.now().date() > check_in_date:
        #     raise serializers.ValidationError('Check-in date must be greater than today.')
        # if timezone.now().date() > check_out_date:
        #     raise serializers.ValidationError('Check-out date must be greater than today.')
        # if check_in_date >= check_out_date:
        #     raise serializers.ValidationError('Check-out date must be greater than check-in date.')

        # return attrs
# class CancelReservationSerializer(serializers.ModelSerializer):
    
#     user = serializers.HiddenField(default = serializers.CurrentUserDefault())
#     class Meta:
#         model = Reservation
#         fields = "__all__"

    # def update(self, instance, validated_data):
    #     # raise Exception(instance)
    #     instance.status = 'canceled'
    #     instance.save()
    #     Room.objects.filter(id = instance.room.pk).update(status = 'V')
    #     return super().update(instance, validated_data)