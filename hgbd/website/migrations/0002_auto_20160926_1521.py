# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelistitem',
            name='text_uk',
            field=models.CharField(max_length=500, verbose_name='Опис пункту'),
        ),
    ]
