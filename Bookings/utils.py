from django.core.mail import send_mail
from django.conf import settings
def send_confrimation_mail(email,token):
    subject = "CONFIRMATION MAIL"
    message =f'Dear user, please verify your request by clicking the link below. http://127.0.0.1:8000/reservations/verify/{token}'
    from_email  = 'falanahotel'
    recipient_list =[email]
    send_mail(subject,message,from_email,recipient_list)



