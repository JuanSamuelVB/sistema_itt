from django.conf.urls import include, url
from .views import *

app_name = 'titulacion'
urlpatterns = [
    url(r'^nuevo/$',newTitulacion.as_view(),name='newTitulacion'),
    url(r'^list/$',listaTitulacion.as_view(),name='lista_titulacion'),
    url(r'^editar/(?P<pk>\d+)/$', editaTitulacion.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', eliminar, name='eliminar'),
]
