# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorias', '0004_seccionmonitoria_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccionmonitoria',
            name='status',
            field=models.CharField(choices=[('aceptada', 'Aceptada'), ('pendiente', 'Pendiente'), ('rechazada', 'Rechazada')], default='pendiente', max_length=10),
        ),
    ]