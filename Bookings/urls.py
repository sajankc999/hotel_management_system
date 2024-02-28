from rest_framework.routers import SimpleRouter
from .views import *
from django.urls import path
router = SimpleRouter()
router.register('booking',BookingViewset,basename='booking')

urlpatterns = [
    # path('booking',BookingViewset.as_view()),
    path('verify/<authtoken>',verify),
    # path('booking',BookingViewset.as_view())
    
]+router.urls
