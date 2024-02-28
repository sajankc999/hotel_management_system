from django.contrib import admin

# Register your models here.
from .models import*
admin.site.register(Room_type)
admin.site.register(Room)