from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

class LogsAnalyzed(models.Model):
    cust_name = models.CharField(max_length=90)
    logs_fileName = models.CharField(max_length=90)
    logs_analyzed_Datetime = models.DateField()
    Logs_FinalFile = models.BinaryField()

