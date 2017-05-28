from django.conf.urls import include, url
from .views import *

app_name = 'creditos'
urlpatterns = [
    url(r'^nueva-actividad/$',newActividad.as_view(),name='newActividad'),
    url(r'^reporte/$',reporteActividad.as_view(),name="reporte_actividad")
]
