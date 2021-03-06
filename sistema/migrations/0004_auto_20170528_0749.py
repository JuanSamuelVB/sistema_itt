# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 07:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20170528_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alumno', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profesor', to=settings.AUTH_USER_MODEL),
        ),
    ]
