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
    form = UserProfileForm(initial={'bio':userProfile.bio,
                                    'studentID':userProfile.studentID,
                                    'picture':userProfile.picture,
                                    'career':userProfile.career,
                                    'university':userProfile.university,
                                    'subjects':userProfile.subjects,
                                    'video':userProfile.video,
                                    'begin_time':userProfile.begin_time,
                                    'end_time':userProfile.end_time})
    return render_to_response('user_profile/update_profile.html', {'form':form}, RequestContext(request))

def profile(request, profile_id):
    if profile_id == "0":
        if request.user.is_authenticated:
            userProfile = UserProfile.objects.get(user=request.user)
    else:
        userProfile = UserProfile.objects.get(pk=profile_id)

    return render_to_response('user_profile/profile.html', {'userProfile': userProfile}, RequestContext(request))

@login_required
def send_update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            userProfile = UserProfile.objects.get(user=request.user)
            bio = form.cleaned_data['bio']
            if 'picture' in request.FILES:
                picture = request.FILES['picture']
                userProfile.picture = picture
            studentID = form.cleaned_data['studentID']
            video = form.cleaned_data['video']
            begintime = form.cleaned_data['begin_time']
            endtime = form.cleaned_data['end_time']

            userProfile.bio = bio
            userProfile.studentID = studentID
            userProfile.video = video
            userProfile.begin_time = begintime
            userProfile.end_time = endtime
            userProfile.save()
            return redirect('/user/profile/' + str(userProfile.id))
    else:
        form = UserProfileForm()

    return redirect('/user/update_profile/')
