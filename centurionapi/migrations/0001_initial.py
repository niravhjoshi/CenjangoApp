# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datewisedetailknownerrcounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('month_name', models.CharField(max_length=50)),
                ('err_name', models.TextField()),
                ('appsrv_name', models.CharField(max_length=50)),
                ('date_date', models.DateField()),
                ('err_counts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='datewiseerrcounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('date_stamp', models.DateField()),
                ('month_name', models.CharField(max_length=50)),
                ('appsrv_name', models.CharField(max_length=50)),
                ('err_counts', models.IntegerField()),
            ],
        ),
    ]
