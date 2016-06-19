from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.personal_profile),
    url(r'^profile/(?P<profile_id>\d+)$', views.profile),
    url(r'^update_profile/$', views.update_profile),
    url(r'^send_update_profile/$', views.send_update_profile),
]
