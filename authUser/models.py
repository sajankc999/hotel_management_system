from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
# Create your models here.hone_number


class CustomManager(UserManager):
    def _create_user(self, email:str,password,username=None , **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if username is None:
            username = email.split("@")[0]
        user = User(email=email,username = username,**extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, email,username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email,username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    full_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 100,unique = True)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS=[]

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_guest = models.BooleanField(default = True)
    is_Receptionist = models.BooleanField(default = False)
    is_Cleaner = models.BooleanField(default = False)
    is_Manager = models.BooleanField(default = False)
    
    date_joined = models.DateField(default = timezone.now)

    objects = CustomManager()

    class Meta:
        permissions = [
            ("view_all_staff", "Can view all staff details"),
            ("change_delete_staff", "Can change or delete staff details"),
            ("view_own_details", "Can view own details"),
        ]
    


     