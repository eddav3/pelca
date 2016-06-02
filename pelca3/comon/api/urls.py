from django.conf.urls import patterns, include, url
from django.conf.urls import url

urlpatterns = patterns('comon.api.views',

   url(r'^hola_mundo_rest/$','hola_mundo')
)