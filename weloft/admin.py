from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Apartment 
from .models import Helpinghand, Apartmentname, PaymentStatus

admin.site.register(Apartmentname)
admin.site.register(PaymentStatus)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('Apt_name','Apt_address', 'Apt_district', 'Apt_phoneNo')

admin.site.register(Apartment,ApartmentAdmin)

class HelpingHandAdmin(admin.ModelAdmin):
    list_display = ('Apt_name','Helper1')

admin.site.register(Helpinghand, HelpingHandAdmin)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','Apt_name','Flat_no']

admin.site.register(CustomUser, CustomUserAdmin)