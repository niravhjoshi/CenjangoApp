# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-11 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProdLogsLoca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=45)),
                ('add_date', models.DateField()),
                ('appsrv_tools_logpath', models.TextField()),
                ('appsrv_localws_logpath', models.TextField()),
                ('log_monitor', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Error_Reporting_JIRA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=45)),
                ('error_name', models.TextField()),
                ('reoprt_date', models.DateField()),
                ('CM_JIRA_issue', models.CharField(max_length=200)),
                ('existing_CM_issue', models.BooleanField()),
                ('error_repeat_app1', models.IntegerField()),
                ('error_repeat_app2', models.IntegerField()),
                ('error_repeat_app98', models.IntegerField()),
                ('error_repeat_app99', models.IntegerField()),
            ],
        ),

    ]
