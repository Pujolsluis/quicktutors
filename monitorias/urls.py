from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.secciones_list, name='secciones_list'),
    url(r'^new/(?P<tutorpk>\d+)/$', views.secciones_new, name='secciones_new'),
    url(r'^seccion/(?P<pk>\d+)/$', views.secciones_detail, name='secciones_detail'),
    url(r'^filtros/(?P<estado>\d+)/$', views.secciones_list_estado, name='secciones_list_estado',),
    url(r'aceptar/(?P<pk>\d+)/$', views.secciones_aceptar, name='secciones_aceptar',),
    url(r'rechazar/(?P<pk>\d+)/$', views.secciones_rechazar, name='secciones_rechazar',),
    url(r'accepted/$', views.secciones_new_accepted, name='secciones_new_accepted',),
    url(r'cancelled/$', views.secciones_new_cancelled, name='secciones_new_cancelled',),
    url(r'online_payment/$', views.secciones_online_payment, name='secciones_online_payment',),
    url(r'onsite_payment/$', views.secciones_onsite_payment, name='secciones_onsite_payment',),

]

