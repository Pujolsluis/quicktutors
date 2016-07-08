from django import forms
from user_profile.models import UserProfile
from user_profile.models import Career
from user_profile.models import University
from user_profile.models import Subject
from django.forms import FileInput


# User profile form
class UserProfileForm(forms.ModelForm):

    studentID = forms.CharField(widget=forms.TextInput, label="ID Estudiantil")
    career = forms.ModelChoiceField(queryset=Career.objects.order_by('name'), label="Carrera")
    university = forms.ModelChoiceField(queryset=University.objects.order_by('name'), label="University")
    picture = forms.ImageField(label=('User Picture'), required=False,
                                    error_messages={'invalid': "Image files only"},
                                    widget=FileInput)



    class Meta:
        model = UserProfile
        fields = [
            'bio',
            'picture',
            'studentID',
            'video',
            'career',
            'university',
            'begin_time',
            'end_time',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setting the form fields classes to materialize css form classes
        for field in self.Meta.fields:
            if field == 'studentID' or field == 'video':
                self.fields[field].widget.attrs.update({
                    'class': 'validate'
                })
            if field == 'bio':
                self.fields[field].widget.attrs.update({
                    'class': 'materialize-textarea'
                })
