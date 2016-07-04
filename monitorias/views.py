from django.shortcuts import render, get_object_or_404
from monitorias.models import SeccionMonitoria
from monitorias.forms import SeccionMonitoriaForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from postman.api import pm_write
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def secciones_list(request):
    # import ipdb
    # ipdb.set_trace()
    secciones = []
    seccionesTodas = []
    seccionesPendientes = []
    seccionesAceptadas = []
    seccionesRechazadas = []
    pendiente = 'pendiente'
    aceptada = 'aceptada'
    rechazada = 'rechazada'
    # integrales = SeccionMonitoria.objects.filter(subject__name="Calculo Integral")
    # integralesSubject = integrales[0].subject
    for i in SeccionMonitoria.objects.all().order_by('-publish_date'):
        if request.user.userprofile.isTutor:

            # Todas las secciones de un usuario que es monitor y estudiante
            if i.estudiante == request.user or i.tutor == request.user:
                seccionesTodas.append(i)

            # secciones pendientes de un usuario que es monitor y estudiante
            if (i.estudiante == request.user or i.tutor == request.user) and i.status == pendiente:
                seccionesPendientes.append(i)

            # secciones aceptadas de un usuario que es monitor y estudiante
            if (i.estudiante == request.user or i.tutor == request.user) and i.status == aceptada:
                seccionesAceptadas.append(i)

            # secciones rechazadas de un usuario que es monitor y estudiante
            if (i.estudiante == request.user or i.tutor == request.user) and i.status == rechazada:
                seccionesRechazadas.append(i)
        else:
            # todas las secciones de un usuario que es estudiante
            if i.estudiante == request.user:
                seccionesTodas.append(i)

            # secciones pendientes de un usuario que es estudiante
            if i.estudiante == request.user and i.status == pendiente:
                seccionesPendientes.append(i)

            # secciones aceptadas de un usuario que es estudiante
            if i.estudiante == request.user and i.status == aceptada:
                seccionesAceptadas.append(i)

            # secciones rechazadas de un usuario que es estudiante
            if i.estudiante == request.user and i.status == rechazada:
                seccionesRechazadas.append(i)

    return render(request, 'monitorias/secciones_list.html', {'seccionesTodas': seccionesTodas,
                                                              'seccionesPendientes': seccionesPendientes,
                                                              'seccionesAceptadas': seccionesAceptadas,
                                                              'seccionesRechazadas': seccionesRechazadas})


@login_required
def secciones_new(request, tutorpk):
    tutor = User.objects.get(pk=tutorpk)
    admin = User.objects.get(username="quicktutors")
    if request.method == "POST":
        form = SeccionMonitoriaForm(request.POST)
        if form.is_valid():
            seccion = form.save(commit=False)
            seccion.estudiante = request.user
            seccion.tutor = tutor
            seccion.save()
            pm_write(admin, tutor, "Nueva Solicitud de monitoria.", "Hola " + tutor.get_short_name() + ",\n\n Tienes una"
                                                                                                       " nueva solicitud"
                                                                                                       " pendiente en tu lista"
                                                                                                       " de monitorias.\n\n"
                                                                                                       "Estudiante: " +
                     seccion.estudiante.get_full_name() + "\nMateria: " + seccion.subject.name + "\n\n-Quicktutors Staff.")
            return redirect('/secciones/')
    else:
        form = SeccionMonitoriaForm()
    return render(request, 'monitorias/secciones_new.html', {'form': form, 'tutor': tutor})

@login_required
# view para que un tutor pueda aceptar una seccion de monitoria
def secciones_aceptar(request, pk):
    seccion = SeccionMonitoria.objects.get(pk=pk)
    seccion.status = "aceptada"
    seccion.save()
    # Enviar mensaje al estudiante con el mensaje de que ha sido rechazada la solicitud
    pm_write(seccion.tutor, seccion.estudiante,
             "Tu seccion de monitoria para la materia " + seccion.subject.name + "ha sido aceptada.",
             "Hola " + seccion.estudiante.get_short_name() + ",\n\n Me complace informarte que estoy disponible"
                                                             " para impartirte tu seccion de monitoria, y me parece bien"
                                                             " el horario seleccionado, asi como lugar de encuentro, estaremos en"
                                                             " contacto por esta via para una futura confirmacion de la"
                                                             " cita.\n\n" \
                                                             "Gracias por utilizar nuestro servicio,\n\n" \
                                                             "-" + seccion.tutor.get_short_name())
    return redirect('/secciones/')

@login_required
# view para que un tutor pueda rechazar una seccion de monitoria
def secciones_rechazar(request, pk):
    seccion = SeccionMonitoria.objects.get(pk=pk)
    seccion.status = "rechazada"
    seccion.save()
    # Enviar mensaje al estudiante con el mensaje de que ha sido rechazada la solicitud
    pm_write(seccion.tutor, seccion.estudiante,
             "Tu seccion de monitoria para la materia " + seccion.subject.name + "ha sido rechazada.",
             "Hola " + seccion.estudiante.get_short_name() +",\n\n Lamento informarte que no podre impartirte" \
                                                           " la seccion de monitoria solicitada ya que no estare" \
                                                           " disponible en ese horario. pero espero que en un futuro" \
                                                           " podamos estudiar juntos!\n\n" \
                                                           "Gracias por utilizar nuestro servicio,\n\n" \
                                                           "-" + seccion.tutor.get_short_name())

    return redirect('/secciones/')
