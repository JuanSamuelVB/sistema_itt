# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nocontrol', models.CharField(max_length=8, null=True)),
                ('nombre', models.CharField(max_length=30, null=True)),
                ('apellidop', models.CharField(max_length=30, null=True)),
                ('apellidom', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='acceso',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='acceso',
            name='profesor',
        ),
        migrations.RemoveField(
            model_name='acceso',
            name='visitante',
        ),
        migrations.RemoveField(
            model_name='visitante',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='visitante',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='visitante',
            name='apellidom',
            field=models.CharField(default='ApellidoM', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitante',
            name='apellidop',
            field=models.CharField(default='ApellidoP', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitante',
            name='detalles',
            field=models.CharField(default='Detalle', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitante',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Acceso',
        ),
    ]
