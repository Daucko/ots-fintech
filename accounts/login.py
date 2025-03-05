from email import message
from turtle import st
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.core.files.base import ContentFile
import pyotp # type: ignore
import qrcode
from io import BytesIO
import base64

import pyotp # type: ignore
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GoogleAuth

User  = get_user_model()

class Enable2FAView(View):
    def get(self, request):
        """Render the enable_2fa.html page when accessed via browser."""
        return render(request, 'home/enable_2fa.html')  # Ensure correct template path

    def post(self, request):
        """Handle 2FA activation via AJAX and return QR code JSON response."""
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required."}, status=401)

        user = request.user
        google_auth, created = GoogleAuth.objects.get_or_create(user=user)

        if google_auth.is_enabled:
            return JsonResponse({"error": "2FA is already enabled."}, status=400)

        # Generate a new secret key
        secret_key = pyotp.random_base32()
        google_auth.secret_key = secret_key
        google_auth.save()

        # Generate QR Code
        totp = pyotp.TOTP(secret_key)
        provisioning_uri = totp.provisioning_uri(name=user.email, issuer_name="YourAppName")
        qr = qrcode.make(provisioning_uri)

        # Convert to Base64
        buffer = BytesIO()
        qr.save(buffer)
        qr_code_base64 = f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"

        return JsonResponse({
            "message": "Scan the QR code with Google Authenticator.",
            "qr_code": qr_code_base64,
        })

class Verify2FAView(View):
    def get(self, request):
        # Render the 2FA verification page
        return render(request, 'home/verify_2fa.html')

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required.'}, status=401)

        otp = request.POST.get('otp')
        user = request.user

        try:
            google_auth = GoogleAuth.objects.get(user=user)
            if google_auth.secret_key:
                # Verify the OTP
                totp = pyotp.TOTP(google_auth.secret_key)
                if totp.verify(otp):
                    google_auth.is_enabled = True
                    google_auth.save()
                    return JsonResponse({'success': 'OTP verified and 2FA enabled.'})
                else:
                    return JsonResponse({'error': 'Invalid OTP.'}, status=400)
            else:
                return JsonResponse({'error': '2FA is not set up for this account.'}, status=400)
        except GoogleAuth.DoesNotExist:
            return JsonResponse({'error': '2FA is not set up for this account.'}, status=400)

class LoginView(View):
    def get(self, request):
        return render(request, "home/login.html")

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            try:
                google_auth = GoogleAuth.objects.get(user=user)
                if google_auth.is_enabled:
                    # Redirect to 2FA verification page
                    request.session['email'] = email
                    request.session['password'] = password
                    return JsonResponse({'error': '2fa_required'})
                else:
                    # Log the user in directly
                    login(request, user)
                    return JsonResponse({'success': 'Logged in Successfully!', 'redirect_url': '/home/'})
            except GoogleAuth.DoesNotExist:
                # Log the user in directly if 2FA is not set up
                login(request, user)
                return JsonResponse({'success': 'Logged in Successfully!', 'redirect_url': '/home/'})
        else:
            return JsonResponse({'error': 'Invalid username or password.'}, status=400)

