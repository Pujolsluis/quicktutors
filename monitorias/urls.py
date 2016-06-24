from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.secciones_list, name='secciones_list'),
    url(r'^new/$', views.secciones_new, name='secciones_new'),
]

