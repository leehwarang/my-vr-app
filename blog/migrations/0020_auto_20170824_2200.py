# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-24 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20170824_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
