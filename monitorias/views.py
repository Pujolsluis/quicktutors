from django.shortcuts import render, get_object_or_404
from monitorias.models import SeccionMonitoria
from monitorias.forms import SeccionMonitoriaForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.

def secciones_list(request):
    # import ipdb
    # ipdb.set_trace()
    secciones = []
    pendiente = "pendiente"
    aceptada = "aceptada"
    rechazada = "rechazada"
    # integrales = SeccionMonitoria.objects.filter(subject__name="Calculo Integral")
    # integralesSubject = integrales[0].subject
    for i in SeccionMonitoria.objects.all().order_by('-publish_date'):
        if request.user.userprofile.isTutor:
            if i.estudiante == request.user or i.tutor == request.user:
                    secciones.append(i)
        else:
            if i.estudiante == request.user:
                secciones.append(i)

    return render(request, 'monitorias/secciones_list.html', {'secciones': secciones, 'pendiente': pendiente, 'aceptada': aceptada, 'rechazada': rechazada})

# Funcion para filtrar lista de secciones de monitorias agendadas

def secciones_list_estado(request, estado):

    secciones = []

    for i in SeccionMonitoria.objects.all().order_by('-publish_date'):
        if request.user.userprofile.isTutor:
            if (i.estudiante == request.user or i.tutor == request.user) and \
                    (i.status == "pendiente" and estado == "1"):
                secciones.append(i)

            if (i.estudiante == request.user or i.tutor == request.user) and \
                    (i.status == "aceptada" and estado == "2"):
                secciones.append(i)

            if (i.estudiante == request.user or i.tutor == request.user) and \
                    (i.status == "rechazada" and estado == "3"):
                secciones.append(i)
        else:
            if (i.estudiante == request.user) and (i.status == "pendiente" and estado == "1"):
                secciones.append(i)

            if (i.estudiante == request.user) and (i.status == "aceptada" and estado == "2"):
                secciones.append(i)

            if (i.estudiante == request.user) and (i.status == "rechazada" and estado == "3"):
                secciones.append(i)

    return render(request, 'monitorias/secciones_list.html', {'secciones': secciones})


def secciones_detail(request,pk):
    seccion = get_object_or_404(SeccionMonitoria, pk=pk)
    return render(request, 'monitorias/secciones_detail.html', {'seccion': seccion})

def secciones_new(request, tutorpk):
    tutor = User.objects.get(pk=tutorpk)
    if request.method == "POST":
        form = SeccionMonitoriaForm(request.POST)
        if form.is_valid():
            seccion = form.save(commit=False)
            seccion.estudiante = request.user
            seccion.tutor = tutor
            seccion.save()
            return redirect('/secciones/')
    else:
        form = SeccionMonitoriaForm()
    return render(request, 'monitorias/secciones_new.html', {'form': form, 'tutor': tutor})

def secciones_aceptar(request, pk):
    seccion = SeccionMonitoria.objects.get(pk=pk)
    seccion.status = "aceptada"
    seccion.save()
    return redirect('/secciones/')

def secciones_rechazar(request, pk):
    seccion = SeccionMonitoria.objects.get(pk=pk)
    seccion.status = "rechazada"
    seccion.save()
    return redirect('/secciones/')