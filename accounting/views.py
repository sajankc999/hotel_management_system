from django.shortcuts import render,HttpResponse
from .models import Invoice
# Create your views here.
from rest_framework.viewsets import generics
from .serializer import *
from Rooms.models import *
from django.core.mail import send_mail
from rest_framework.response import Response
class InvoiceView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        inc= Invoice.objects.filter(reservation__user = self.request.user)
        if inc:
            return inc
        
    

def payment(request,authtoken):
    inv = Invoice.objects.filter(payment_id=authtoken).first()
    if inv:
        inv.is_paid = True
        res = Reservation.objects.filter(id = inv.pk).first()
        print(res)
        room = Room.objects.filter(id=res.room.pk).update(status='R')
        print(room)
        
        inv.save()
        
        return HttpResponse(' verification successfull.your room is now reserved')





