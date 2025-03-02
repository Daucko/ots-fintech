from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from .mailer_otp_sender import send_otp

from django.contrib.auth import get_user_model

User  = get_user_model()




class RegiserView(View):
    def get(self, request):
        return render(request, 'home/signup.html')
    

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password1 = request.POST['password2']
        account_type = request.POST['account_type']


        if not username or not  email or not  password1 or not password or not phone:
            return JsonResponse({'error': 'Please fill all the form fields'}, status=400)
        
        if password != password1:
             return JsonResponse({'error': 'Password do not match'}, status=400)
        
        if User.objects.filter(email=email).exists():
             return JsonResponse({'error': 'Email already exists'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        

        if User.objects.filter(phone=phone).exists():
            return JsonResponse({'error': 'Phone number already exists'}, status=400)
        
        user = User.objects.create(
            username=username,
            email=email,
            phone=phone,
            account_type= account_type ,
            password= make_password(password)
        )
        send_otp(email)
        return JsonResponse({'success': 'User Register Successfully'}, status=201)


        




        
        
           

