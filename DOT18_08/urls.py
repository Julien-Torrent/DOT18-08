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

    url(r'^api/setSpeed/(?P<speed>\d{0,3})', app.api.setSpeed, name='setSpeed'),
    url(r'^api/getSpeed', app.api.getSpeed, name='getSpeed'),

    url(r'^api/setLeds/(?P<ledsStatus>\d)', app.api.setLeds, name='setLeds'),
    url(r'^api/getLeds', app.api.getLeds, name='getLeds'),

    url(r'^api/nextMove', app.api.nextMove, name='nextMove'),
    url(r'^api/turnLeft/(?P<angle>\d{0,3})', app.api.turnLeft, name='turnLeft'),
    url(r'^api/turnRight/(?P<angle>\d{0,3})', app.api.turnRight, name='turnRight'),
    url(r'^api/forward', app.api.forward, name='forward'),
    url(r'^api/backward', app.api.backward, name='backward'),

    url(r'^api/sendStatus', app.api.sendStatus, name='sendStatus'),

    # Admin :
    url(r'^admin/', admin.site.urls),
]