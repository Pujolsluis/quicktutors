from django import forms
from monitorias.models import SeccionMonitoria


# Seccion de monitoria form
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
        # Setting the fields to the materialize css form classes
        for field in self.Meta.fields:
            if field == 'description':
                self.fields[field].widget.attrs.update({
                'class': 'validate'
                })
