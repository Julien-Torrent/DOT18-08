"""
Definition of urls for DOT18_08.
"""

from datetime import datetime
from django.conf.urls import url

import django.contrib.auth.views
import app.views


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Pages:
    url(r'^$', app.views.home, name='home'),
    url(r'^command$', app.views.command, name='command'),

    # API :
    url(r'^api/setMode/(?P<mode>\d)', app.api.setMode, name='setMode'),
    url(r'^api/getMode', app.api.getMode, name='getMode'),

    url(r'^api/setSpeed/(?P<speed>\d{0,4})', app.api.setSpeed, name='setSpeed'),
    url(r'^api/getSpeed', app.api.getSpeed, name='getSpeed'),

    # Admin :
    url(r'^admin/', admin.site.urls),
]