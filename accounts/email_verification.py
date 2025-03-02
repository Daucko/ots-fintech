from django.views.generic import View
from django.http import JsonResponse
from .models import User, OTPCODE
from .mailer_otp_sender import send_otp
from django.shortcuts import render


class EmailVerificationView(View):
    def get(self, request):
        return render(request, 'home/otpverify.html')


    def post(self, request):
        otp_user = request.POST["otp_code"]

        if not otp_user:
            return JsonResponse({"error": "OTP is required"}, status=400)
        
        try:
            user_otp_records = OTPCODE.objects.get(email_otp=otp_user)
            # The user that is associated with the OTP code
            user = user_otp_records.user
        except OTPCODE.DoesNotExist:
            return JsonResponse({"error": "Invalid OTP code"}, status=400)



        if user_otp_records.is_otp_expired():
            send_otp(user.email)
            return JsonResponse({"error": "OTP has expired. A new OTP has been sent to your email"}, status=400)

        if user.email_verified:
            return JsonResponse({"error": "Email already verified"})
        
        user.email_verified = True
        user.save()

        return JsonResponse({"success": "Email verified successfully"}, status=201)