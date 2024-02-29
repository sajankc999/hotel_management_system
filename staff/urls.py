from rest_framework.routers import SimpleRouter
from .views import *
from django.urls import path
router = SimpleRouter()
router.register('profile',Staffview,basename='profile')
router.register('shifts',ShiftView,basename='shifts')
router.register('task',Taskview,basename='task')
urlpatterns = [
    # path("emp",Staffview.as_view()),
]+router.urls
