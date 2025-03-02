from .home  import HomepageView
from .register import RegiserView
from .login import LoginView
from django.urls import path
from .email_verification import EmailVerificationView



urlpatterns = [

       path('', HomepageView.as_view(), name='home'),
       path('register', RegiserView.as_view(), name='register'),
       path('login', LoginView.as_view(), name='login'),
       path('verify-email', EmailVerificationView.as_view(), name='verify'),
       

    
]
