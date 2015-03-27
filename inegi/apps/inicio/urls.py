from django.conf.urls import patterns, include, url
from .views import Inicio, Exito, AltaWindows, Configuracion, Equipos, AltaParche,listaParches, AltaEquipo

urlpatterns = patterns('',
    # Examples:
   	url(r'^$', Inicio.as_view()),
   	#url(r'^$', AltaUpdate , name="inicio"),
   	#url(r'^$', AltaWindows , name="inicio"),
   	url(r'^windows/$', AltaWindows , name="windows"),
   	url(r'^exito/$', Exito.as_view(), name="exito"),
   	url(r'^configuracion/$', Configuracion.as_view(), name="config"),
   	url(r'^equipos/$', Equipos.as_view(), name="equipos"),
   	url(r'^parche/$', AltaParche, name="parches"),
   	url(r'^listaParches/$', listaParches.as_view(), name="listaParches"),
      url(r'^AltaEquipo/$', AltaEquipo, name="AltaEquipo"),

)
