from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required



def quicktutorsApp(request):
    if request.user.is_authenticated():
        userProfile = UserProfile.objects.get(user=request.user)
        return {'USER_PROFILE': userProfile, 'ESTADO_PENDIENTE': "aceptada"}
    else:
        return {'USER_PROFILE': "None"}
