from user_profile.models import UserProfile


def quicktutorsApp(request):
    userProfile = UserProfile.objects.get(user=request.user)
    return {'USER_AVATAR': userProfile.picture.url}
