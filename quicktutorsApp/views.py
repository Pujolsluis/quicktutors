from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile
# Create your views here.

def undercons_page(request):
    return render(request, 'quicktutorsApp/undercons_page.html')

def home_page(request):
    return render(request, 'quicktutorsApp/index.html')

def dashboard(request):
    return render(request, 'quicktutorsApp/dashboard.html')

