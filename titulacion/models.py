from django.db import models
from django.utils import timezone

class Titulacion(models.Model):
    proyecto = models.CharField(max_length=50)

    alumno = models.ForeignKey('sistema.Alumno',
                                 on_delete=models.CASCADE)

    presidente = models.ForeignKey('sistema.Profesor',
                                 on_delete=models.CASCADE, related_name = 'presidente+',default=1)
    secretario = models.ForeignKey('sistema.Profesor',
                                 on_delete=models.CASCADE, related_name = 'secretario+',default=1)
    vocal = models.ForeignKey('sistema.Profesor',
                                 on_delete=models.CASCADE, related_name = 'vocal+', default=1)
    suplente = models.ForeignKey('sistema.Profesor',
                                 on_delete=models.CASCADE, related_name = 'suplente+', default=1)

    fecha_inicio = models.DateField(default=timezone.now())
    fecha_fin = models.DateField(default=timezone.now())

    revision_1 = models.DateField(default=timezone.now())
    revision_2 = models.DateField(default=timezone.now())


    def __str__(self):
        return '%s : %s' % (self.proyecto, self.alumno)
