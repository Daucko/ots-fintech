from .home  import HomepageView
from .register import RegisterView
from .login import LoginView, Verify2FAView, Enable2FAView
from django.urls import path
from .email_verification import EmailVerificationView



urlpatterns = [ 

       path('', HomepageView.as_view(), name='home'),
       path('register', RegisterView.as_view(), name='register'),
       path('login', LoginView.as_view(), name='login'),
       path('verify-email', EmailVerificationView.as_view(), name='verify'),
       # path('profile/', ProfileView.as_view(), name='profile'),
       path('enable-2fa/', Enable2FAView.as_view(), name='enable_2fa'),
       path('verify-2fa/', Verify2FAView.as_view(), name='verify_2fa'),
       

    
]
