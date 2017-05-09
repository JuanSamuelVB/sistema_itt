from django.db import models

class Titulacion(models.Model):
    proyecto = models.CharField(max_length=50)
    profesor = models.ForeignKey('sistema.Profesor', 
                                 on_delete=models.CASCADE)
    alumno = models.ForeignKey('sistema.Alumno', 
                                 on_delete=models.CASCADE)
