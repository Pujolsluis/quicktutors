from django import forms
from monitorias.models import SeccionMonitoria


class SeccionMonitoriaForm(forms.ModelForm):

    class Meta:
        model = SeccionMonitoria

        fields = [
            'university',
            'reunionsite',
            'subject',
            'description',
            'begin_timeDay',
            'hours_wanted',
            'payment_method',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
            })
