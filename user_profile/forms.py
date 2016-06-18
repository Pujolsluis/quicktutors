from django import forms
from user_profile.models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user','subjects',)
