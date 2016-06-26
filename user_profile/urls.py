from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.personal_profile, name='profile'),
    url(r'^profile/(?P<profile_id>\d+)$', views.profile, name='tutor_profile'),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
    url(r'^send_update_profile/$', views.send_update_profile),
    url(r'^search/$', views.profile_search_page, name='search_page'),
    url(r'^search/(?P<subject>[\w\s]+)/$', views.profile_filter_subject, name='search_page_filter'),
]
