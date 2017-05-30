from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

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

@python_2_unicode_compatible
class Alumno(models.Model):
    user = models.OneToOneField(User, related_name='alumno')
    apellidos = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    semestre = models.IntegerField(choices=SEMESTRES, default=1)

    def __str__(self):
        return self.apellidos + " " + self.nombre

@python_2_unicode_compatible
class Profesor(models.Model):
    user = models.OneToOneField(User, related_name='profesor')
    apellidos = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    creditos_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.apellidos + " " + self.nombre
