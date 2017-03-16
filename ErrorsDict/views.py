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
def errorsdict_add(request):
    return render_to_response('errorsdictAdd.html')

def errorsdict_show(request):
    return render_to_response('errorsdictShow.html')

def errorsdict_update(request):
    return render_to_response('errorsdictUpdate.html')

