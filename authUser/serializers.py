from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

user = get_user_model()
class UserRegisterSerailizer(serializers.Serializer):
    full_name = serializers.CharField(max_length = 150,required = True)
    phone_number = serializers.CharField(max_length = 10)
    email = serializers.EmailField(max_length=100 ,required = True)
    password = serializers.CharField(max_length =100 , required = True)
    # def validate_email(self,value):
    #     if user.objects.filter(email=value).exists():
    #         raise serializers.ValidationError({"error":"user with email already exists"})
    #     return value
    def validate_email(self,value):
        if user.objects.filter(email=value).exists():
            raise serializers.ValidationError({"error":"user with email already exists"})
        return value
    def validate_password(self,value):
        if len(value)<8 or len(value)>65:
            raise serializers.ValidationError({"error":"password must be between 8 and 65 characters."})
        return value 
     
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =user
        fields=['email','password']

class UserSerializer(serializers.ModelField):
    class Meta:
        model = user
        fields =['full_name','email','phone_number']