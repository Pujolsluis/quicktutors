from django.db import models
from django.contrib.auth.models import User
from user_profile.models import University, ReunionSite, Subject
from django.utils import timezone
# Create your models here.

def affiliate_company_directory(self,filename):
    return 'quicktutorsApp/media/affiliate_company/{0}'.format(filename)


class SeccionMonitoria(models.Model):
    ACEPTADA = 'aceptada'
    PENDIENTE = 'pendiente'
    RECHAZADA = 'rechazada'

    ESTADO_SECCION_MONITORIA = (
        (ACEPTADA, 'Aceptada'),
        (PENDIENTE, 'Pendiente'),
        (RECHAZADA, 'Rechazada'),

    )
    status = models.CharField(
        max_length=10,
        choices=ESTADO_SECCION_MONITORIA,
        default=PENDIENTE,

    )
    estudiante = models.ForeignKey(User, related_name='seccionmonitoria_estudiante')
    tutor = models.ForeignKey(User, related_name='seccionmonitoria_tutor')
    university = models.ForeignKey(University)
    reunionsite = models.ForeignKey(ReunionSite)
    subject = models.ForeignKey(Subject)
    description = models.TextField(default='')
    begin_timeDay = models.DateTimeField(default=timezone.now)
    end_timeDay = models.DateTimeField(null=True)
    hours_wanted = models.IntegerField(default='2')
    publish_date = models.DateTimeField(default=timezone.now)
    seccion_payed = models.BooleanField(default=False)

    ONLINE = 'online'
    EFECTIVO = 'efectivo'

    FORMA_DE_PAGO = (
        (ONLINE, 'online'),
        (EFECTIVO, 'efectivo'),

    )
    payment_method = models.CharField(
        max_length=10,
        choices=FORMA_DE_PAGO,
        default=ONLINE,
    )

    def __unicode__(self):
        return "Sección: " + self.estudiante.get_short_name() + " / " + self.tutor.get_short_name() + " de " + self.subject.name + " - " + self.begin_timeDay.__str__()

    def __str__(self):
        return "Sección: " + self.estudiante.get_short_name() + " / " + self.tutor.get_short_name() + " de " + self.subject.name + " - " + self.begin_timeDay.__str__()

class AffiliateCompany(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=affiliate_company_directory, default='reunion_site_directory/no-image.jpg')
    address = models.TextField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
