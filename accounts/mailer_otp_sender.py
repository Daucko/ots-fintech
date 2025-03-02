# from urllib.parse import uses_fragment
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
import pyotp  # type: ignore
from .models import User,OTPCODE

# Function to generate otp code to user
def generate_otp():
    otpcode = pyotp.TOTP(pyotp.random_base32())
    return otpcode.now()


def send_otp(email):
    subject = "One Time Password (OTP) Generation"
    otp = generate_otp()
    user = User.objects.get(email=email)
    otp_record, create_opt = OTPCODE.objects.get_or_create(user=user)
    otp_record.email_otp = otp
    otp_record.created_at = timezone.now()
    otp_record.save()


    # Compose email body
    body = f"Hi {user.username},\n\nYour OTP is {otp}.\n\nThis expires in 30 minutes. Please do not share this with anyone.\n\nThanks,\n{settings.EMAIL_HOST_USER}"
    email_from = settings.EMAIL_HOST_USER
    email_sender = EmailMessage(subject=subject, from_email=email_from, body=body, to=[email] )
    email_sender.send(fail_silently=True)