from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import generics
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class FeedbackView(generics.ListCreateAPIView,generics.DestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def delete(self, request, *args, **kwargs):
        feedback = Feedback.objects.filter(user = self.request.user).first()
        if feedback:
            feedback.delete()
            return Response('successfully deleted')
        else:
            return Response('you donot have any feedbacks yet')
        

