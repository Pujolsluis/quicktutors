from django.shortcuts import render, get_object_or_404
from monitorias.models import SeccionMonitoria
from monitorias.forms import SeccionMonitoriaForm
from django.shortcuts import redirect
# Create your views here.

def secciones_list(request):
    # import ipdb
    # ipdb.set_trace()
    secciones = set()
    # integrales = SeccionMonitoria.objects.filter(subject__name="Calculo Integral")
    # integralesSubject = integrales[0].subject
    for i in SeccionMonitoria.objects.all():
        if request.user.userprofile.isTutor:
            if i.estudiante == request.user or i.tutor == request.user:
                    secciones.add(i)
        else:
            if i.estudiante == request.user:
                secciones.add(i)

    return render(request, 'monitorias/secciones_list.html', {'secciones': secciones})

def secciones_detail(request,pk):
    seccion = get_object_or_404(SeccionMonitoria, pk=pk)
    return render(request, 'monitorias/secciones_detail.html', {'seccion': seccion})

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
