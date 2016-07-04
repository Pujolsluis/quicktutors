from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.secciones_list, name='secciones_list'),
    url(r'^new/(?P<tutorpk>\d+)/$', views.secciones_new, name='secciones_new'),
    url(r'^seccion/(?P<pk>\d+)/$', views.secciones_detail, name='secciones_detail'),
    url(r'aceptar/(?P<pk>\d+)/$', views.secciones_aceptar, name='secciones_aceptar',),
    url(r'rechazar/(?P<pk>\d+)/$', views.secciones_rechazar, name='secciones_rechazar',)

]

