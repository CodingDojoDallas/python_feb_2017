# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170306_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default="2017-01-17 01:00"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favorite',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
