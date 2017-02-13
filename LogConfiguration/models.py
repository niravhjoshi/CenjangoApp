from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

class temptab(models.Model):
    cust_name = models.CharField(max_length=45)
    err_cnts = models.IntegerField()
    newerr_cnts = models.IntegerField()

class CustomerProdLogsLoca(models.Model):
    cust_name = models.CharField(max_length=45)
    add_date = models.DateField()
    appsrv_tools_logpath = models.TextField()
    appsrv_localws_logpath = models.TextField()
    log_monitor = models.BooleanField(default=True)

class Error_Reporting_JIRA(models.Model):
    cust_name = models.CharField(max_length=45)
    error_name = models.TextField()
    reoprt_date = models.DateField()
    CM_JIRA_issue = models.CharField(max_length=200)
    existing_CM_issue = models.BooleanField()
    existing_CM_issue_resolved = models.BooleanField(default=True)
    error_repeat_app1 = models.IntegerField()
    error_repeat_app2 = models.IntegerField()
    error_repeat_app98 = models.IntegerField()
    error_repeat_app99 = models.IntegerField()

