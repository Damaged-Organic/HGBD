# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160928_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicelistitem',
            old_name='text',
            new_name='text_uk',
        ),
    ]
