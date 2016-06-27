from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.questions_list, name='questions_list'),
]
