import os
import sys
import os.path
#import subprocess
from django.conf import settings
from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from ingreso.models import *
# Create your views here.

def ingreso(request):
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'numcontrol':
            nocontrol = request.POST['control']
            try:
                alumno = usuarios.objects.get(nocontrol=nocontrol)
                return redirect('ingreso:alumno', alumno.id)
            except Exception:
                return redirect('ingreso:ingreso')
        if action == 'visitante':
            return redirect('ingreso:visita')
    return render(request, 'ingreso/ingreso.html')

def alumno(request, alumno):
    alum = usuarios.objects.get(id = alumno)
    return render(request, 'ingreso/alumno.html', {'usuario':alum})

def visita(request):
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'visit':
            vis = visitante()
            vis.nombre = request.POST['Nombre']
            vis.apellidop = request.POST['ApellidoP']
            vis.apellidom = request.POST['ApellidoM']
            vis.detalles = request.POST['descricion']
            vis.save()
            return redirect('ingreso:alumno')
        if action == 'est':
            return redirect('ingreso:ingreso')
    return render(request, 'ingreso/visita.html')

def registro(request):
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'regist':
            act = usuarios()
            act.nocontrol = request.POST['cont']
            act.nombre = request.POST['nomb']
            act.apellidop = request.POST['pat']
            act.apellidom = request.POST['mat']
            act.save()
            return redirect('ingreso:registro')
        if action == 'est':
            return redirect('ingreso:ingreso')
    return render(request, 'ingreso/registro.html')
