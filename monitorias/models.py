from django.db import models
from django.contrib.auth.models import User
from user_profile.models import University, ReunionSite, Subject
from django.utils import timezone
# Create your models here.


class SeccionMonitoria(models.Model):
    estudiante = models.ForeignKey(User, related_name='seccionmonitoria_estudiante')
    tutor = models.ForeignKey(User, related_name='seccionmonitoria_tutor')
    university = models.ForeignKey(University)
    reunionsite = models.ForeignKey(ReunionSite)
    subject = models.ForeignKey(Subject)
    description = models.TextField
    begin_timeDay = models.DateTimeField(default=timezone.now)
    end_timeDay = models.DateTimeField(null=True)

    def __unicode__(self):
        return "Sección: " + self.estudiante.get_short_name() + " / " + self.tutor.get_short_name() + " de " + self.subject.name + " - " + self.begin_timeDay.__str__()

    def __str__(self):
        return "Sección: " + self.estudiante.get_short_name() + " / " + self.tutor.get_short_name() + " de " + self.subject.name + " - " + self.begin_timeDay.__str__()

