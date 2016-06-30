from django.shortcuts import render_to_response, redirect
from django.http import  HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile
from django.shortcuts import render
from user_profile.forms import UserProfileForm
from django.template import RequestContext
# Create your views here.


@login_required
def update_profile(request):
    userProfile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(initial={
                                    'user': userProfile.user,
                                    'bio': userProfile.bio,
                                    'studentID': userProfile.studentID,
                                    'picture': userProfile.picture,
                                    'career': userProfile.career,
                                    'university': userProfile.university,
                                    'subjects': userProfile.subjects.all,
                                    'video': userProfile.video,
                                    'begin_time': userProfile.begin_time,
                                    'end_time': userProfile.end_time})
    return render(request, 'user_profile/update_profile.html', {'form': form, 'userProfile': userProfile})

@login_required
def personal_profile(request):
    if request.user.is_authenticated():
        userProfile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_profile/profile.html', {'userProfile': userProfile})

@login_required
def profile(request, profile_id):
    if profile_id == "0" or profile_id == '':
        if request.user.is_authenticated:
            userProfile = UserProfile.objects.get(user=request.user)
    else:
        userProfile = UserProfile.objects.get(pk=profile_id)


    return render(request, 'user_profile/profile.html', {'userProfile': userProfile})


@login_required
def send_update_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            if 'picture' in request.FILES:
                picture = request.FILES['picture']
                profile.picture = picture
            form.save()

            return redirect('/user/profile/')
    else:
        form = UserProfileForm(instance=profile)

    return redirect('/user/update_profile/')

@login_required
def profile_search_page(request):
    userProfiles = UserProfile.objects.all().filter(isTutor=True)
    return render(request, 'quicktutorsApp/search_page.html', {'userProfiles': userProfiles})

@login_required
def profile_filter_subject(request, subject):
    userProfiles = UserProfile.objects.all().filter(isTutor=True).filter(subjects__name=subject)
    return render(request, 'quicktutorsApp/search_page.html', {'userProfiles': userProfiles})

