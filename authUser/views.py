from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet,generics
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerailizer,UserLoginSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view 
# Create your views here.
user_obj = get_user_model()

@api_view(['POST'])
def register(request):
    serializer = UserRegisterSerailizer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    password = serializer.validated_data.get('password')
    full_name = serializer.validated_data.get('full_name')
    phone_number = serializer.validated_data.get('phone_number')
    user = user_obj.objects.create_user(email=email, password=password,full_name=full_name,phone_number=phone_number)

    if user:
       
        return Response('user has been created')
    return Response("something went wrong")
    

@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    user = authenticate(username = email,password=password)
    if user:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({
            "username":user.get_username(),
            "token":token.key,
        })
    return  Response(user)




        
