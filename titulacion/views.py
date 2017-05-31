from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy

from sistema.models import Alumno, Profesor
from .models import Titulacion
from .forms import TitulacionForm

class newTitulacion(CreateView):
    template_name = 'titulacion/nuevo-titulacion.html'
    '''form_class = TitulacionForm'''
    model = Titulacion
    fields = '__all__'
    success_url = reverse_lazy('titulacion:lista_titulacion')

    def form_valid(self, form):
        titu = form.save(commit=False)
        titu.profesor = self.request.user.profesor
        return super(newTitulacion, self).form_valid(form)

class listaTitulacion(ListView):
    template_name='titulacion/list.html'
    model = Titulacion
    fields='__all__'
    queryset = Titulacion.objects.all()

class editaTitulacion(UpdateView):
    model = Titulacion
    fields='__all__'
    template_name='titulacion/edit.html'

class detalleTitulacion(DetailView):
    model = Titulacion
    fields='__all__'
    template_name='titulacion/edit.html'

def editar(request, pk):
    titusE = get_object_or_404(Titulacion, pk=pk)
    titusE.delete()

    return redirect('titulacion:editar')

def eliminar(request, pk):
    titus = get_object_or_404(Titulacion, pk=pk)
    titus.delete()

    return redirect('titulacion:lista_titulacion')
