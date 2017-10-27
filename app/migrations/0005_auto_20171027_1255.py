# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171027_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='khoa',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='khoa',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='khoa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='khoa',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]