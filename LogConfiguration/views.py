from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render,render_to_response
import random
import datetime
import time
import models
from django.db.models import Sum, Avg
import urllib2,simplejson
import operator
from models import CustomerProdLogsLoca
# Create your views here.
def customer_add(request):
    return render_to_response('CustomerAdd.html')

def customer_list(request):
    try:
        listofcust = CustomerProdLogsLoca.objects.all()
    except:
        raise Http404("Sorry There are no data added into CustomerProdLogsLoca Yet")
    #Return  Page

    return render(request,'CustomerList.html',{"data":listofcust})


def Errors_Dict(request):
    return render_to_response('ErrorsDict.html')

def NewLog_File(request):
    return render_to_response('NewLogFile.html')

