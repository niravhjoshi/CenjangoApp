from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from binaryfield import BinaryField
from django.db import models
from Cenjango import settings
# Create your models here.

class LogsAnalyzed(models.Model):
    Cust_name = models.CharField(max_length=90)
    app_srv_name = models.CharField(max_length=90)
    log_file_date = models.DateField()
    logs_fileName = models.CharField(max_length=90)
    logs_analyzed_Datetime = models.DateField()
    Logs_FinalFile = models.FilePathField(path=settings.BASE_DIR,
                                     max_length=250, allow_files=True,
                                     recursive=True, allow_folders=False,blank=True)


