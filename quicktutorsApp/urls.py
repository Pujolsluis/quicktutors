from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from user_profile import views

urlpatterns = [
    url(r'^$', views.home_page, name='undercons_page'),
    url(r'^home/$', views.home_page, name='home_page'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

