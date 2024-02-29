from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet,GenericViewSet,generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .utils import *
from datetime import datetime

# Create your views here.
from .models import *
from .serializer import *
class BookingViewset(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    def list(self,request,*args, **kwargs):
        # raise Exception(self.request.user)
        reservation = Reservation.objects.filter(user = self.request.user).first()
        if not reservation:
            return Response("you dont have any reservations")
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        user = self.request.user
        data = request.data
        # raise Exception(data)
        if data:
            room_id = data.get("room_id")
            check_in_date = data.get('check_in_date')
            check_out_date = data.get('check_out_date')
            room = Room.objects.filter(pk = room_id).first()
            # raise Exception(room)
            if room:
                past_reservation = Reservation.objects.filter(room = room_id)
                if past_reservation:
                    if datetime.now() ==check_out_date:
                        room.status ='V'
                        room.save()
                if room.status is not 'V':
                    return Response('this room is not available please select another room according to your requirement')
                reservation=Reservation.objects.create(user=user,room=room,check_in_date=check_in_date,check_out_date=check_out_date,status="inactive")
                room.status ="P"
                room.save()
                # raise Exception(reservation)
                send_confrimation_mail(email = user.email, token = reservation.confirmation_token)
                return Response('we have sent you a confirmation link .Please check your mail')
        else:
            return Response('no room exists')
        return Response('data error')
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CancelReservationSerializer
        return ReservationSerializer    
    
    def update(self, request, *args, **kwargs):
        reservation = Reservation.objects.filter(user = self.request.user , room = request.data.get('room_id')).first()
        room = Room.objects.filter(id =request.data.get('room_id') ).filter()
        if reservation:
            reservation.room = Room.objects.get(id =request.data.get('room_id') )
            reservation.check_in_date = request.data.get('check_in_date')
            reservation.check_out_date = request.data.get('check_out_date')
            reservation.save()
            return Response(' you booking has been updated')
        return Response('you dont have any reservations')


def verify(request,authtoken):
    try:
        reservation = Reservation.objects.filter(confirmation_token= authtoken).first()
        
        if reservation:
            reservation.status ="active"
            reservation.save()
            # raise Exception(reservation.room.pk)
            room=Room.objects.filter(id = reservation.room.pk).first()
            room.status='B'
            room.save()
            
            return HttpResponse("successfully registered")
        else:
            return HttpResponse("wrong token")
    except Exception as e:
        return HttpResponse("something went worng try again later")
        