# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-22 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170722_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='classification',
            field=models.CharField(choices=[('XBOX', 'XBOX'), ('CARDBOARD', 'CARDBOARD')], default=360, max_length=20),
        ),
    ]
