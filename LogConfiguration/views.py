from django.shortcuts import render
from django.shortcuts import render,render_to_response
import random
import datetime
import time
import models
from django.db.models import Sum, Avg
import urllib2,simplejson
import operator

# Create your views here.
def customer_add(request):
    return render_to_response('CustomerAdd.html')

def Errors_Dict(request):
    return render_to_response('ErrorsDict.html')

def NewLog_File(request):
    return render_to_response('NewLogFile.html')

