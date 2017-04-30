from django.shortcuts import render
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import request
import random
import datetime
import time
from models import ErrorsDict
from centurionapi.models import datewisedetailknownerrcounts
from django.db.models import Sum, Avg
import urllib2,simplejson
import operator
from django.http import Http404,HttpResponse
import urllib2,simplejson
from itertools import groupby
from collections import Counter,defaultdict
from operator import itemgetter
import operator
import itertools
from chartit import DataPool, Chart,PivotDataPool,PivotChart
from centurionapi.decorators import add_source_code_and_doc







# Create your views here.
def errorsdict_add(request):
    return render_to_response('errorsdictAdd.html')


def Single_errors_graph2(request):

    errname= request.GET.get('err_name')
    request.session['errnamesess'] = errname
    print request.session['errnamesess']
    ds = PivotDataPool(
        series=[
            {'options': {
                'source': datewisedetailknownerrcounts.objects.filter(err_name=errname),
                'categories': ['appsrv_name'],
                'legend_by': 'appsrv_name'},
                'terms': {'Total_ErrCounts': Sum('err_counts')
                          }}])

    pivcht = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column',
                'stacking': True,
                'xAxis': 0,
                'yAxis': 0},
                'terms': ['Total_ErrCounts']}])

    # end_code
    return render_to_response('ErrorsSingleGraph.html',
                          {
                              'chart_list': pivcht,
                              'code': "newcode",
                              'title': "SingleErrorChart",
                              'doc': "This Chart Displays selected error name pivot group by App Server Name",
                              'sidebar_items': "SIdeBarItem"})


def Single_errors_graph2_ViewByMonth(request):
    if 'errnamesess' in request.session:
        errname = request.session['errnamesess']
    else:
        print "SOmething wrong in session variable"
    ds = PivotDataPool(
        series=[
            {'options': {
                'source': datewisedetailknownerrcounts.objects.filter(err_name=errname),
                'categories': ['month_name'],
                'legend_by': 'month_name'},
                'terms': {'Total_ErrCounts': Sum('err_counts')
                          }}])

    pivcht = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column',
                'stacking': True,
                'xAxis': 0,
                'yAxis': 0},
                'terms': ['Total_ErrCounts']}])

    # end_code
    return render_to_response('ErrorsSingleGraph.html',
                          {
                              'chart_list': pivcht,
                              'code': "newcode",
                              'title': "Error View by Monthwise:-",
                              'doc': "This Chart Displays selected error name pivot group by Month Name",
                              'sidebar_items': "SIdeBarItem"})



def Single_errors_graph2_viewByDates(request):
    if 'errnamesess' in request.session:
        errname = request.session['errnamesess']
    else:
        print "SOmething wrong in session variable"
    ds = PivotDataPool(
        series=[
            {'options': {
                'source': datewisedetailknownerrcounts.objects.filter(err_name=errname),
                'categories': ['date_date'],
                'legend_by': 'date_date'},
                'terms': {'Total_ErrCounts': Sum('err_counts')
                          }}])

    pivcht = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column',
                'stacking': True,
                'xAxis': 0,
                'yAxis': 0},
                'terms': ['Total_ErrCounts']}])

    # end_code
    return render_to_response('ErrorsSingleGraph.html',
                          {
                              'chart_list': pivcht,
                              'code': "newcode",
                              'title': "Error view by Date:-",
                              'doc': "This Chart Displays selected error name pivot group by Date",
                              'sidebar_items': "SIdeBarItem"})



def Single_errors_graph2_viewByCustomer(request):
    if 'errnamesess' in request.session:
        errname = request.session['errnamesess']
    else:
        print "SOmething wrong in session variable"
    ds = PivotDataPool(
        series=[
            {'options': {
                'source': datewisedetailknownerrcounts.objects.filter(err_name=errname),
                'categories': ['cust_name'],
                'legend_by': 'cust_name'},
                'terms': {'Total_ErrCounts': Sum('err_counts')
                          }}])

    pivcht = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column',
                'stacking': True,
                'xAxis': 0,
                'yAxis': 0},
                'terms': ['Total_ErrCounts']}])

    # end_code
    return render_to_response('ErrorsSingleGraph.html',
                          {
                              'chart_list': pivcht,
                              'code': "newcode",
                              'title': "Error view by Customer Name:-",
                              'doc': "This Chart Displays selected error name pivot group by Customer Name",
                              'sidebar_items': "SIdeBarItem"})




def errorsdict_show(request):
    try:
        listofErrs = ErrorsDict.objects.all()
    except:
        raise Http404("Sorry There are no data added into Error Dictionary Yet")

    context = listofErrs
    return render(request,'errorsdictShow.html',{"data":listofErrs})

def errorsdict_update(request):
    return render_to_response('errorsdictUpdate.html')

