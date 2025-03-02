from django.contrib import admin
from .models import User, PersonalAccount, BusinessAccount, OTPCODE, UserAuthSettings

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_superuser', 'email_verified']


@admin.register(PersonalAccount)
class PersonalAccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'image']


@admin.register(BusinessAccount)
class BusinessAccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'company_name', 'registration_number']


@admin.register(OTPCODE)
class OTPCODEAdmin(admin.ModelAdmin):
    list_display = ['user', 'email_otp', 'phone_otp', 'created_at']

# @admin.register(UserAuthSettings)
# class UserAuthSettingsAdmin(admin.ModelAdmin):
#     list_display = ['user', 'email_otp', 'phone_otp', 'created_at']

admin.site.register(UserAuthSettings)



