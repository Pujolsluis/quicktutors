from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from user_profile import views

# Homepage, dashboard & underconstruction url.
urlpatterns = [
    # Change this view to views.undercons_page to use the underconstruction page with this url.
    url(r'^$', views.home_page, name='undercons_page'),
    url(r'^home/$', views.home_page, name='home_page'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),


]

# Static and media url's
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

