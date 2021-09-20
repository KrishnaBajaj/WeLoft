from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from .models import Helpinghand, Facilities, Maintenance, PaymentStatus

class IndexView(generic.DetailView):
    template_name = 'index.html'


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'weloft/signup.html'

class HelpinghandsView(generic.CreateView):
    model = Helpinghand
    fields = '__all__'
    template_name = 'weloft/helpinghands.html'

	
class OverviewView(generic.CreateView):
    model = Helpinghand
    fields = '__all__'
    template_name = 'weloft/overview.html'	

class BookingsView(generic.CreateView):
    model = Facilities
    fields = '__all__'
    template_name = 'weloft/bookings.html'

class MaintenanceView(generic.CreateView):
    model = Maintenance
    fields = '__all__'
    template_name = 'weloft/maintenance.html'

class PaymentView(generic.CreateView):
    model = PaymentStatus
    fields = '__all__'
    template_name = 'weloft/paymentdetails.html'
