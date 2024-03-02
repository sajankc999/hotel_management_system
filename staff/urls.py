from rest_framework.routers import SimpleRouter
from .views import *
from django.urls import path
router = SimpleRouter()
router.register('emp',Staffadminview,basename='emp')
router.register('shifts',ShiftView,basename='shifts')
# router.register('task',Taskview,basename='task')
router.register('taskadmin',Taskadminview,basename='task-admin')
urlpatterns = [
    path("profile",Staffview.as_view()),
    path('my-task',Taskview.as_view()),
]+router.urls
