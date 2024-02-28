from django.shortcuts import render,HttpResponse
from .models import Invoice
# Create your views here.
from rest_framework.viewsets import generics
from .serializer import *
from Rooms.models import *
from django.core.mail import send_mail

class InvoiceView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.filter(reservation__user = self.request.user)
    




