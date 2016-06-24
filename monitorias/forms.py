from django import forms
from monitorias.models import SeccionMonitoria


class SeccionMonitoriaForm(forms.ModelForm):

    class Meta:
        model = SeccionMonitoria

        fields = [
            'tutor',
            'university',
            'reunionsite',
            'subject',
            'description',
            'begin_timeDay',
            'end_timeDay',
        ]

