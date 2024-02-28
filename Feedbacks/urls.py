from django.urls import path
from .views import *

urlpatterns = [
    path("review",FeedbackView.as_view()),
]
