from django import forms
from user_profile.models import UserProfile
from user_profile.models import Career
from user_profile.models import University
from user_profile.models import Subject

class UserProfileForm(forms.ModelForm):

    studentID = forms.CharField(widget=forms.TextInput, label="ID Estudiantil")
    career = forms.ModelChoiceField(queryset=Career.objects.order_by('name'), label="Carrera")
    university = forms.ModelChoiceField(queryset=University.objects.order_by('name'), label="University")
    subjects = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Subject.objects.order_by('name'), label="Materias que domina")


    class Meta:
        model = UserProfile
        fields = [
            'bio',
            'picture',
            'studentID',
            'video',
            'career',
            'university',
            'subjects',
            'begin_time',
            'end_time',
        ]

