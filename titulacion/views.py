from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from sistema.models import Alumno, Profesor
from .models import Titulacion

class newTitulacion(CreateView):
    template_name = 'titulacion/nuevo-titulacion.html'
    model = Titulacion
    fields = ['proyecto', 'alumno', 'presidente', 'secretario', 'vocal', 'suplente', 'fecha_inicio', 'fecha_fin']
    success_url = reverse_lazy('sistema:profile')

    def form_valid(self, form):
        titu = form.save(commit=False)
        titu.profesor = self.request.user.profesor
        return super(newTitulacion, self).form_valid(form)

class listaTitulacion(ListView):
    template_name='titulacion/list.html'
    model = Titulacion
    fields='__all__'
    queryset = Titulacion.objects.all()

def eliminar(request, pk):
    titus = get_object_or_404(Titulacion, pk=pk)
    titus.delete()

    return redirect('titulacion:lista_titulacion')
