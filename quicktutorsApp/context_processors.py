from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required
from monitorias.models import Publicity



def quicktutorsApp(request):
    if request.user.is_authenticated():
        userProfile = UserProfile.objects.get(user=request.user)
        publicity_list = Publicity.objects.all()
        return {'USER_PROFILE': userProfile, 'PUBLICITY_LIST': publicity_list}
    else:
        return {'USER_PROFILE': "None"}
