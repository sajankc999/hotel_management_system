from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Invoice
from Bookings.models import Reservation
from Rooms.models import *
from django.core.mail import send_mail
@receiver(post_save,sender = Reservation)
def Reservation_Created(sender,instance,*args, **kwargs):
    print(instance)
    if Invoice.objects.filter(reservation=instance).exists():
        pass
    else:
        reservation = Reservation.objects.filter(id = instance.pk).first()
        Check_in = reservation.check_in_date
        check_out = reservation.check_out_date
        days = (check_out -Check_in).days
        room = Room.objects.filter(id = reservation.room.pk).first()
        room_type = Room_type.objects.filter(id= room.type.pk).first()
        total_amount = (room_type.room_charge +room_type.service_charge)*days
        special_discount = room_type.discount
        paid_amount = total_amount-((special_discount*total_amount)/100)
        Invoice.objects.create(
            reservation = instance,
            total_amount=total_amount,
            special_discount=special_discount,
            paid_amount=paid_amount,
        )
        # invoice = Invoice.objects.filter(reservation = instance).first()
        




