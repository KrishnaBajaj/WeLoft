# weloft/urls.py
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.urls import path
from . import views

#app_name = 'weloft'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('helpinghands/', views.HelpinghandsView.as_view(), name='hhv'),
	path('overview/', views.OverviewView.as_view(), name='overview'),
    path('calendar/', include('cal.urls',namespace="cal")),
    path('bookings/', views.BookingsView.as_view(), name='booking'),
    path('messages/', include('postman.urls',namespace='coms')),
    path('maintenance/', views.MaintenanceView.as_view(), name='maintenance'),
    path('paymentdetails/', views.PaymentView.as_view(), name='payd'),
]