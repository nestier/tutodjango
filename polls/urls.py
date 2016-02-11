from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^create$', views.create_question, name='create_question'),
    url(r'^(?P<question_id>[0-9]+)/edit/$', views.edit_question, name='edit'),
    url(r'^(?P<question_id>[0-9]+)/delete$', views.delete_question, name='delete_question'),
    url(r'^choice/(?P<question_id>[0-9]+)/create/$', views.create_choice, name='create_choice'),
    url(r'^(?P<question_id>[0-9]+)/(?P<choice_id>[0-9]+)/edit/$', views.edit_choice, name='edit_choice'),
    url(r'^(?P<question_id>[0-9]+)/(?P<choice_id>[0-9]+)/delete$', views.delete_choice, name='delete_choice'),


        ]
