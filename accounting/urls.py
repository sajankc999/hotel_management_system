from django.urls import path
from .views import *

urlpatterns = [
    path('bill',InvoiceView.as_view()),
    path('payment/verify/<authtoken>',payment)
]

