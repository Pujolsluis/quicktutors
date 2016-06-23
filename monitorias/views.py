from django.shortcuts import render
from monitorias.models import SeccionMonitoria
# Create your views here.

def secciones_list(request):
    secciones = SeccionMonitoria.objects.all()
    return render(request, 'monitorias/secciones_list.html', {'secciones': secciones})
