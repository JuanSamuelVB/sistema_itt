from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.
class Welcome(TemplateView):
	template_name = 'sistema/index.html'
