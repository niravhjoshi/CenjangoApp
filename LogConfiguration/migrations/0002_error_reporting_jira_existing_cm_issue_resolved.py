# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogConfiguration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='error_reporting_jira',
            name='existing_CM_issue_resolved',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
