from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.secciones_list, name='secciones_list'),
    url(r'^new/(?P<tutorpk>\d+)/$', views.secciones_new, name='secciones_new'),
    url(r'^seccion/(?P<pk>\d+)/$', views.secciones_detail, name='secciones_detail'),
    url(r'^filtros/(?P<estado>\d+)/$', views.secciones_list_estado, name='secciones_list_estado',),

]

