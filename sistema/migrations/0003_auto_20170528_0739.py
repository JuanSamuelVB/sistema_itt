# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 07:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistema', '0002_auto_20170514_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='semestre',
            field=models.IntegerField(choices=[(1, '1 semestre'), (2, '2 semestre'), (3, '3 semestre'), (4, '4 semestre'), (5, '5 semestre'), (6, '6 semestre'), (7, '7 semestre'), (8, '8 semestre'), (9, '9 semestre'), (10, '10 semestre'), (11, '11 semestre'), (12, '12 semestre')], default=1),
        ),
    ]
