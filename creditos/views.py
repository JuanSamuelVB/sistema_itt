from django.shortcuts import render, get_object_or_404, redirect
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


def solicitar(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)

    if not request.user.alumno in actividad.alumnos.all():
        actividad.alumnos.add(request.user.alumno)

    return redirect('creditos:reporte_actividad')
