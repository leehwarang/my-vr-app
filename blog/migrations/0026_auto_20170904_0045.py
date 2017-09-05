# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-03 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20170904_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='hashtag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='hashtag_set',
        ),
        migrations.DeleteModel(
            name='Hashtag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]