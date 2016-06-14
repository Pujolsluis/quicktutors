from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.undercons_page, name='undercons_page'),
    url(r'^home/$', views.home_page, name='home_page'),
    url(r'^search/$', views.search_page, name='search_page'),
]
