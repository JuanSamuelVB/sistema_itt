# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_auto_20170528_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='creditos_admin',
            field=models.BooleanField(default=False),
        ),
    ]
