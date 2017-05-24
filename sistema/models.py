from django.db import models

SEMESTRES = (
        (1, '1 semestre'),
        (2, '2 semestre'),
        (3, '3 semestre'),
        (4, '4 semestre'),
        (5, '5 semestre'),
        (6, '6 semestre'),
        (7, '7 semestre'),
        (8, '8 semestre'),
        (9, '9 semestre'),
        (10, '10 semestre'),
        (11, '11 semestre'),
        (12, '12 semestre'),
    )

class Alumno(models.Model):
    apellidos = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    semestre = models.IntegerField(choices=SEMESTRES, default=1)

    def __unicode__(self):
        return self.apellidos

class Profesor(models.Model):
    apellidos = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)

    def __unicode__(self):
        return self.apellidos
