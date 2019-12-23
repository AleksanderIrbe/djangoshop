
from django.urls import path

from django.conf.urls import url, include
from ecommapp.views import *


urlpatterns = [
    path('', base_view, name='base'),
]