# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-21 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcategory', models.CharField(choices=[('SPOT', 'SPOT'), ('ACCOMODATION', 'ACCOMODATION'), ('RESTAURANT', 'RESTAURANT')], default='SPOT', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField(default='내용을 입력해주세요.', verbose_name='CONTENT')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Country')),
                ('postcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
    ]
