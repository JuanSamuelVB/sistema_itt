from django.conf.urls import include, url
from .views import *

app_name = 'creditos'
urlpatterns = [
    url(r'^nueva-actividad/$',newActividad.as_view(),name='newActividad'),
    url(r'^solicitar/(?P<pk>\d+)/$', solicitar, name='solicitar'),
    url(r'^reporte/$',reporteActividad.as_view(),name="reporte_actividad"),
    url(r'^reporte/por-aprobar$', porAprobarActividad.as_view(), name="por_aprobar"),
    url(r'^aprobar/(?P<pk>\d+)/$', aprobar, name='aprobar'),
    url(r'^eliminar/(?P<pk>\d+)/$', eliminar, name='eliminar'),
    url(r'^actividad/(?P<pk>\d+)/$', detalleActividad.as_view(), name="actividad"),
    url(r'^actividad/(?P<actividad_pk>\d+)/aceptar-alumno/(?P<alumno_pk>\d+)/$', aceptar_alumno, name="aceptar_alumno"),
]
