# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-14 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='semestre',
            field=models.IntegerField(choices=[(1, b'1 semestre'), (2, b'2 semestre'), (3, b'3 semestre'), (4, b'4 semestre'), (5, b'5 semestre'), (6, b'6 semestre'), (7, b'7 semestre'), (8, b'8 semestre'), (9, b'9 semestre'), (10, b'10 semestre'), (11, b'11 semestre'), (12, b'12 semestre')], default=1),
        ),
    ]