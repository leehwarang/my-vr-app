# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-03 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20170904_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hash',
            field=models.TextField(default=True, max_length=100),
        ),
    ]
