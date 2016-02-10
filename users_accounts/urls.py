from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^logout/$', auth_views.logout,
            {
             'next_page':'/',
            },name='logout'),
    url(r'^login/$', auth_views.login,
            {
             'template_name':'registration/login.html',
            },name='login'),
    url(r'^edit$', views.edit_user, name='edit_user'),
    url(r'^new$', views.new_user, name='new_user'),
  #  url(r'^', include('django.contrib.auth.urls'))
        ]
