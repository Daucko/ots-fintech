from email import message
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse

import pyotp # type: ignore
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserAuthSettings

User  = get_user_model()




class LoginView(View):
    def get(self, request):
        return render(request, 'home/login.html')
    
    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        otp_code = request.POST["otp_code", None]

        if not email or not password:
            return JsonResponse({"error": "Email and password is required"}, status=400)
        
        user = authenticate(request, email=email, password=password)

        if user:
            user_settings, _ = UserAuthSettings.objects.get_or_create(user=user)

            # If Google Auth is required, verify OTP
            if user_settings.google_auth_required:
                if not otp_code:
                    return JsonResponse({"error": "OTP is required"}, status=400)
                
                secret_key = "YOUR_SECRET_KEY" # Store per user in DB for better security
                totp = pyotp.TOTP(secret_key)

                if not totp.verify(otp_code):
                    return JsonResponse({"error": "Invalid OTP code"}, status=400)
                

            login(request, user)
            return JsonResponse({"success": "User logged in successfully"}, status=200)
        
        else:
            return JsonResponse({"error": "Invalid email or password"}, status=400)
        
            

