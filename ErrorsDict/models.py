from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

class ErrorsDict(models.Model):
    Error_name = models.TextField(default='')
    Error_reportDate=models.DateField(default='')
