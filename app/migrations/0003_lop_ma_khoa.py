# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171027_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='lop',
            name='ma_khoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lop_khoa', to='app.Khoa'),
        ),
    ]
