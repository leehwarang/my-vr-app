# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-22 08:16
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
