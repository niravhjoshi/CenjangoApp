from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

class CustomerProdLogsLoca(models.Model):
    cust_name = models.CharField(max_length=45,default='')
    srv1_name_dir = models.CharField(max_length=80,default='')
    srv2_name_dir = models.CharField(max_length=80,default='')
    srv98_name_dir = models.CharField(max_length=80,default='')
    srv99_name_dir = models.CharField(max_length=80,default='')
    add_date = models.DateField(default='')
    appsrv_tools_logpath = models.TextField(default='')
    appsrv_localws_logpath = models.TextField(default='')
    log_monitor = models.BooleanField(default=True)

class Error_Reporting_JIRA(models.Model):
    cust_name = models.CharField(max_length=45,default='')
    error_name = models.TextField(default='')
    reoprt_date = models.DateField(default='')
    CM_JIRA_issue = models.CharField(max_length=200,default='')
    existing_CM_issue = models.BooleanField(default=False)
    existing_CM_issue_resolved = models.BooleanField(default=True)
    error_repeat_app1 = models.IntegerField(default=0)
    error_repeat_app2 = models.IntegerField(default=0)
    error_repeat_app98 = models.IntegerField(default=0)
    error_repeat_app99 = models.IntegerField(default=0)

