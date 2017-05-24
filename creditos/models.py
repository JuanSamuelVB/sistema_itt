from django.db import models

ESTATUS = (
        (1, 'Por aprobar'),
        (2, 'Aprobada'),
        (3, 'Terminada'),
    )

class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    total_creditos = models.IntegerField()
    estatus = models.IntegerField(choices=ESTATUS, default=1)
    profesor = models.ForeignKey('sistema.Profesor', 
                                 on_delete=models.CASCADE)
    alumnos = models.ManyToManyField('sistema.Alumno')

    def __unicode__(self):
        return self.nombre
        
