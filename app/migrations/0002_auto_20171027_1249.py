# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 12:49
from __future__ import unicode_literals

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinhvien',
            name='avatar',
            field=models.ImageField(blank=True, default='avt.png', null=True, upload_to=app.models.content_file_name),
        ),
        migrations.AddField(
            model_name='sinhvien_monhoc',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
