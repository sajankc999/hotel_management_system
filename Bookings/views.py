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
from django.utils import timezone
from accounting.models import Invoice
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
            # raise Exception(check_in_date)
            room = Room.objects.filter(pk = room_id).first()
            # if timezone.now() > datetime.strptime(check_in_date, "%Y-%m-%d"):
            #     return Response('Check-in date must be greater than today.')
            # if timezone.now().date() > check_out_date:
            #     return Response('Check-out date must be greater than today.')
            
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
    # def get_serializer_class(self):
    #     if self.request.method == "DELETE":
    #         return CancelReservationSerializer
    #     return ReservationSerializer    
    
    def update(self, request, *args, **kwargs):
        reservation = Reservation.objects.filter(user = self.request.user , room = request.data.get('room_id')).first()
        room = Room.objects.filter(id =request.data.get('room_id') ).first()
        if reservation:
            reservation.room = Room.objects.get(id =request.data.get('room_id') )
            reservation.check_in_date = request.data.get('check_in_date')
            reservation.check_out_date = request.data.get('check_out_date')
            reservation.status =request.data.get('status')

            reservation.save()
            if reservation.status=='canceled':
                room.status = 'V'
                room.save()
            return Response(' you booking has been updated')
        return Response('you dont have any reservations')
    def destroy(self, request, *args, **kwargs):
        return Response('this is not available')

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
            inv = Invoice.objects.filter(reservation=reservation).first()
            p_id=inv.payment_id
            send_payment_mail(email = reservation.user.email ,token=p_id)
            return HttpResponse("successfully booked . we have sent you another link to verify your payment please check you mailbox")
        else:
            return HttpResponse("wrong token")
    except Exception as e:
        return HttpResponse("something went worng try again later")
        

# class cancelView(generics.UpdateAPIView):
#     queryset=Reservation.objects.all()
#     serializer_class = CancelReservationSerializer

#     def update(self, request, *args, **kwargs):
#         try:
#             room_id = request.get('room')
#             res= Reservation.objects.filter(user=self.request.user,room = room_id).first()
#             if res:
#                 res.status='inactive'
#                 Room.objects.filter(id = res.room.pk).update(status = 'V')
#                 res.save()
#         except Exception as e:
#             return Response(e)

# def Cancel_reservation(request,res_id):
#     if request.user:
#         res = Reservation.objects.filter(user=request.user,id = res_id)
#         if res:
#             res.status='canceled'
#             Room.objects.filter(id = res.room.pk).update(status = 'V')
#             res.save() 
#         else:
#             return HttpResponse("please check the inputs")
#     else:
#         return HttpResponse('no user provided')