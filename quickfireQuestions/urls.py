from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.questions_list, name='questions_list'),
    url('^(?P<pk>\d+)/$', views.questions_detail, name='questions_detail'),
    url('^new/$', views.questions_new, name='questions_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.questions_edit, name='questions_edit'),
]
