from django.shortcuts import render

# Create your views here.

def undercons_page(request):
    return render(request, 'quicktutorsApp/undercons_page.html')

