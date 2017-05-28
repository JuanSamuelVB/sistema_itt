from django.db import models
from django.utils.encoding import python_2_unicode_compatible

ESTATUS = (
        (1, 'Por aprobar'),
        (2, 'Aprobada'),
        (3, 'Terminada'),
    )

@python_2_unicode_compatible
class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    total_creditos = models.IntegerField()
    estatus = models.IntegerField(choices=ESTATUS, default=1)
    profesor = models.ForeignKey('sistema.Profesor',
                                 on_delete=models.CASCADE)
    candidatos = models.ManyToManyField('sistema.Alumno',
            blank=True,
            related_name='actividades_solicitada')
    alumnos = models.ManyToManyField('sistema.Alumno',
            blank=True,
            related_name='actividades')

    def __str__(self):
        return self.nombre
