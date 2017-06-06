"""Defines URL Patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login page;because it's using a library defined view,
    # the template is also added as an argument
    url(
        r'^login/$',
        login,
        {'template_name': 'users/login.html'},
        name='login'
    ),

    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),

    # Registration page
    url(r'^register/$', views.register, name='register'),
]
