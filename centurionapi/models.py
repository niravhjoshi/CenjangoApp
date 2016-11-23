from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class datewisedetailknownerrcounts(models.Model):
    cust_name = models.CharField(max_length=50)
    month_name = models.CharField(max_length=50)
    err_name = models.TextField()
    appsrv_name = models.CharField(max_length=50)
    date_date = models.DateField()
    err_counts = models.IntegerField()

    def __str__(self):
        return "Customer Name=> {} |  Months Name=> {} | Error Name=> {} | App Server Name=> {} |  Date of Occurance=> {} | Errors Count=> {} |".format(self.cust_name,self.month_name,self.err_name,self.appsrv_name,self.date_date,self.err_counts)

@python_2_unicode_compatible
class datewiseerrcounts(models.Model):
    cust_name = models.CharField(max_length=50)
    date_stamp = models.DateField()
    month_name = models.CharField(max_length=50)
    appsrv_name = models.CharField(max_length=50)
    err_counts = models.IntegerField()

    def __str__(self):
        return "List {}".format(self.cust_name)