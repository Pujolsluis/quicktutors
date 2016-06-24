from django.shortcuts import render
from monitorias.models import SeccionMonitoria
from monitorias.forms import SeccionMonitoriaForm
from django.shortcuts import redirect
# Create your views here.

def secciones_list(request):
    secciones = SeccionMonitoria.objects.all()
    return render(request, 'monitorias/secciones_list.html', {'secciones': secciones})

def secciones_new(request):
    if request.method == "POST":
        form = SeccionMonitoriaForm(request.POST)
        if form.is_valid():
            seccion = form.save(commit=False)
            seccion.estudiante = request.user
            seccion.save()
            return redirect('secciones_list')
    else:
        form = SeccionMonitoriaForm()
    return render(request, 'monitorias/secciones_new.html', {'form': form})
