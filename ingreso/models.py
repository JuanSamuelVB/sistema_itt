from django.db import models

class Visitante(models.Model):
    apellidos = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Acceso(models.Model):
    profesor = models.ForeignKey('sistema.Profesor', 
                                 on_delete=models.CASCADE)
    alumno = models.ForeignKey('sistema.Alumno', 
                                 on_delete=models.CASCADE)
    visitante = models.ForeignKey('ingreso.Visitante', 
                                 on_delete=models.CASCADE)
