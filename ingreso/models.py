from django.db import models

class usuarios(models.Model):
	nocontrol = models.CharField(max_length=8,null=True)
	nombre = models.CharField(max_length=30,null=True)
	apellidop = models.CharField(max_length=30,null=True)
	apellidom = models.CharField(max_length=30,null=True)

class visitante(models.Model):
	nombre = models.CharField(max_length=30)
	apellidop = models.CharField(max_length=30)
	apellidom = models.CharField(max_length=30)
	detalles = models.CharField(max_length=50)
