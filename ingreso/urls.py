from django.conf.urls import url
from ingreso.views import *

app_name = 'ingreso'
urlpatterns = [
	url(r'^ingreso$', ingreso, name='ingreso'),
	url(r'^alumno/(?P<alumno>\w+?)$', alumno, name='alumno'),
	url(r'^visita$', visita, name='visita'),
	url(r'^registro$', registro, name='registro'),
]
