from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Actividad

class newActividad(CreateView):
    template_name = 'creditos/nueva-actividad.html'
    model = Actividad
    fields = ['nombre', 'total_creditos', 'descripcion']
    success_url = reverse_lazy('sistema:profile')

    def form_valid(self, form):
        act = form.save(commit=False)
        act.profesor = self.request.user.profesor
        return super(newActividad, self).form_valid(form)

class reporteActividad(ListView):
    template_name='creditos/reporte.html'
    model = Actividad
    fields='__all__'

class porAprobarActividad(ListView):
    template_name='creditos/por_aprobar.html'
    queryset = Actividad.objects.filter(estatus=1)

class detalleActividad(DetailView):
    template_name = 'creditos/actividad.html'
    model = Actividad


def solicitar(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)

    if not request.user.alumno in actividad.candidatos.all():
        actividad.candidatos.add(request.user.alumno)

    return redirect('creditos:reporte_actividad')

def aprobar(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    actividad.estatus = 2
    actividad.save()

    return redirect('creditos:reporte_actividad')

def eliminar(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    actividad.delete()

    return redirect('creditos:por_aprobar')
