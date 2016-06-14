from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.undercons_page, name='undercons_page'),
]
