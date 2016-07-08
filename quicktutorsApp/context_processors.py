from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required
from monitorias.models import Publicity

# logged in user context processor so the profile is always available to all templates, and also the publicity list.
def quicktutorsApp(request):
    if request.user.is_authenticated():
        userProfile = UserProfile.objects.get(user=request.user)
        publicity_list = Publicity.objects.all()
        return {'USER_PROFILE': userProfile, 'PUBLICITY_LIST': publicity_list}
    else:
        return {'USER_PROFILE': "None"}
