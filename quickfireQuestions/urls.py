from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.questions_list, name='questions_list'),
    url('^(?P<pk>\d+)/$', views.questions_detail, name='questions_detail'),
    url('^new/$', views.questions_new, name='questions_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.questions_edit, name='questions_edit'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment_to_questions, name='add_comment_to_questions'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^comment/(?P<pk>\d+)/correctanswer/$', views.comment_correct_answer, name='comment_correct_answer'),
    url(r'^quickfire/(?P<option>[\w\s]+)/$', views.quickfire_pay, name='quickfire_pay'),
    url(r'accepted/$', views.questions_pay_accepted, name='questions_pay_accepted',),
    url(r'cancelled/$', views.questions_pay_cancelled, name='questions_pay_cancelled',),
]
