# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-04 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20170905_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, max_length=40, to='blog.Tag'),
        ),
    ]
