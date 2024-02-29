from .views import *
from django.urls import path
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('types',RoomTypeView,basename='types')
urlpatterns = [
    path('room',Roomview.as_view()),
    
]+router.urls
