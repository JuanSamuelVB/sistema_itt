from django.shortcuts import render
from django.views.generic import TemplateView,CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import *

class newActividad(CreateView):
	template_name = 'creditos/nueva-actividad.html'
	model = Actividad
	fields = '__all__'
	success_url = reverse_lazy('Welcome_View')

class reporteActividad(ListView):
	template_name='creditos/reporte.html'
	model = Actividad
	fields='__all__'
