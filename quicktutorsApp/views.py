from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile
# Create your views here.

# Under construction page render
def undercons_page(request):
    return render(request, 'quicktutorsApp/undercons_page.html')

# Homepage render
def home_page(request):
    return render(request, 'quicktutorsApp/home_page.html')

# Dashboard render
def dashboard(request):
    return render(request, 'quicktutorsApp/dashboard.html')

