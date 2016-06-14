from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def undercons_page(request):
    return render(request, 'quicktutorsApp/undercons_page.html')

def home_page(request):
    return render(request, 'quicktutorsApp/home_page.html')

@login_required()
def search_page(request):
    users = User.objects.all()
    return render(request, 'quicktutorsApp/search_page.html', {'users': users})
