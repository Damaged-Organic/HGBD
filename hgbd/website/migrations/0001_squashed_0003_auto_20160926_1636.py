# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 13:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('website', '0001_initial'), ('website', '0002_auto_20160926_1521'), ('website', '0003_auto_20160926_1636')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('label_uk', models.CharField(max_length=20, verbose_name='Ярлик')),
                ('title_uk', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text_uk', models.TextField(max_length=500, verbose_name='Текст')),
            ],
            options={
                'order_prefix': '     ',
                'verbose_name_plural': '     Блок "Компанія"',
                'verbose_name': 'Блок "Компанія"',
            },
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_uk', models.CharField(max_length=200, verbose_name='Опис переваги')),
            ],
            options={
                'verbose_name_plural': 'Переваги',
                'verbose_name': 'Перевага',
            },
        ),
        migrations.CreateModel(
            name='BenefitsContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title_uk', models.CharField(max_length=50, verbose_name='Заголовок')),
            ],
            options={
                'order_prefix': '    ',
                'verbose_name_plural': '    Блок "Переваги"',
                'verbose_name': 'Блок "Переваги"',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=19, verbose_name='Телефон')),
                ('email', models.CharField(max_length=254, verbose_name='E-mail')),
                ('address_uk', models.CharField(max_length=300, verbose_name='Адреса')),
            ],
            options={
                'verbose_name_plural': 'Контакти',
                'verbose_name': 'Контакт',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_uk', models.CharField(max_length=100, verbose_name='Посада')),
                ('name_uk', models.CharField(max_length=200, verbose_name='Імʼя')),
                ('surname_uk', models.CharField(max_length=200, verbose_name='Прізвище')),
                ('photo', models.ImageField(upload_to='employee/photos/', verbose_name='Фотографія')),
            ],
            options={
                'verbose_name_plural': 'Співробітники',
                'verbose_name': 'Співробітник',
            },
        ),
        migrations.CreateModel(
            name='GetInTouchContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title_uk', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text_uk', models.TextField(max_length=500, verbose_name='Текст')),
                ('link_title_uk', models.CharField(max_length=20, verbose_name='Заголовок посилання')),
            ],
            options={
                'order_prefix': ' ',
                'verbose_name_plural': ' Блок "Звʼязок"',
                'verbose_name': 'Блок "Звʼязок"',
            },
        ),
        migrations.CreateModel(
            name='IntroContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('headline_uk', models.CharField(max_length=100, verbose_name='Слоган')),
            ],
            options={
                'order_prefix': '      ',
                'verbose_name_plural': '      Блок "Вступ"',
                'verbose_name': 'Блок "Вступ"',
            },
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='Значення')),
                ('description_uk', models.CharField(max_length=50, verbose_name='Опис')),
            ],
            options={
                'verbose_name_plural': 'Цифри',
                'verbose_name': 'Цифра',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uk', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('headline_uk', models.CharField(max_length=200, verbose_name='Слоган')),
                ('description_uk', models.CharField(max_length=500, verbose_name='Короткий опис')),
                ('about_label_uk', models.CharField(max_length=20, verbose_name='Ярлик')),
                ('about_description_uk', models.TextField(max_length=1500, verbose_name='Детальний опис')),
                ('hint_title_uk', models.CharField(max_length=100, verbose_name='Заголовок визначення')),
                ('hint_description_uk', models.CharField(max_length=500, verbose_name='Текст визначення')),
                ('image_main', models.ImageField(upload_to='service/images/main/', verbose_name='Головне зображення')),
                ('image_list', models.ImageField(upload_to='service/images/list/', verbose_name='Зображення до списку')),
            ],
            options={
                'verbose_name_plural': 'Сервіси',
                'verbose_name': 'Сервіс',
            },
        ),
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_uk', models.CharField(max_length=50, verbose_name='Ярлик')),
                ('title_uk', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Service')),
            ],
            options={
                'verbose_name_plural': 'Списки характеристик сервісу',
                'verbose_name': 'Список характеристик сервісу',
            },
        ),
        migrations.CreateModel(
            name='ServiceListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_uk', models.CharField(max_length=500, verbose_name='Опис пункту')),
                ('service_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.ServiceList')),
            ],
            options={
                'verbose_name_plural': 'Пункти списку характеристик сервісу',
                'verbose_name': 'Пункт списку характеристик сервісу',
            },
        ),
        migrations.CreateModel(
            name='ServicesContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('label_uk', models.CharField(max_length=20, verbose_name='Ярлик')),
                ('title_uk', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text_uk', models.TextField(max_length=500, verbose_name='Текст')),
            ],
            options={
                'order_prefix': '   ',
                'verbose_name_plural': '   Блок "Сервіси"',
                'verbose_name': 'Блок "Сервіси"',
            },
        ),
        migrations.CreateModel(
            name='TeamContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('label_uk', models.CharField(max_length=20, verbose_name='Ярлик')),
                ('title_uk', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text_uk', models.TextField(max_length=500, verbose_name='Текст')),
            ],
            options={
                'order_prefix': '  ',
                'verbose_name_plural': '  Блок "Команда"',
                'verbose_name': 'Блок "Команда"',
            },
        ),
        migrations.AlterModelTable(
            name='aboutcontent',
            table='content_about',
        ),
        migrations.AlterModelTable(
            name='benefit',
            table='benefits',
        ),
        migrations.AlterModelTable(
            name='benefitscontent',
            table='content_benefits',
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contacts',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employees',
        ),
        migrations.AlterModelTable(
            name='getintouchcontent',
            table='content_get_in_touch',
        ),
        migrations.AlterModelTable(
            name='introcontent',
            table='content_intro',
        ),
        migrations.AlterModelTable(
            name='number',
            table='numbers',
        ),
        migrations.AlterModelTable(
            name='service',
            table='services',
        ),
        migrations.AlterModelTable(
            name='servicelist',
            table='services_lists',
        ),
        migrations.AlterModelTable(
            name='servicelistitem',
            table='services_lists_items',
        ),
        migrations.AlterModelTable(
            name='servicescontent',
            table='content_services',
        ),
        migrations.AlterModelTable(
            name='teamcontent',
            table='content_team',
        ),
    ]
