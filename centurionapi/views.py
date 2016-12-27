from django.shortcuts import render,render_to_response
import random
import datetime
import time
import urllib2,simplejson
from itertools import groupby
from collections import Counter,defaultdict
from operator import itemgetter
import operator
import itertools

#Home page rendering method
def home(request):
    return render_to_response('centurionapi/Home.html')

def about(request):
    return render_to_response('centurionapi/about.html')

def get_customererrpiechart(request):

    url = "http://127.0.0.1:8000/centurionapi/dwercnt?fields=cust_name,err_counts"
    response = urllib2.urlopen(url)
    data = simplejson.load(response)
    xdata = []
    ydata = []
    # group the departments in lists
    list1 = []
    for key, items in itertools.groupby(data, operator.itemgetter('cust_name')):
        list1.append(list(items))
    #print "After grouping the list by customer_name:"
    #pprint.pprint(list1)  # test
    #print "-" * 50

    # Sum of error counts by customer group
    err_list = []
    for item in list1:
        # get customer name:
        customername = item[0]['cust_name']
        #print  customername
        size = len(item)
        #print  size
        sum = 0
        for k in range(size):
            sum += int((item[k]['err_counts']))
        err_list.append((customername, sum))
    #print err_list
    for item in err_list:
        #print "CustomerName   %s has an total error  %d" % (item[0], item[1])
        xdata.append(item[0])
        ydata.append(item[1])
    print xdata
    print ydata

    color_list = ['#5d8aa8', '#e32636', '#efdecd', '#ffbf00', '#ff033e', '#a4c639',
                  '#b2beb5', '#8db600', '#7fffd4', '#ff007f', '#ff55a3', '#5f9ea0']
    extra_serie = {
        "tooltip": {"y_start": "", "y_end": " Errors Count"},
        "color_list": color_list
    }
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'  # container name

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('JsonDatapiechart.html', data)




app1url = "http://127.0.0.1:8000/centurionapi/dwercnt?fields=appsrv_name,err_counts&appsrv_name=App1"
app2url = "http://127.0.0.1:8000/centurionapi/dwercnt?fields=appsrv_name,err_counts&appsrv_name=App2"
app98url = "http://127.0.0.1:8000/centurionapi/dwercnt?fields=appsrv_name,err_counts&appsrv_name=App98"
app99url = "http://127.0.0.1:8000/centurionapi/dwercnt?fields=appsrv_name,err_counts&appsrv_name=App99"


def get_appsrvnameerrcntschart(request):
    xdata = []
    ydata = []
    appurls=[]
    appurls.append(app1url)
    appurls.append(app2url)
    appurls.append(app98url)
    appurls.append(app99url)
    print appurls
    for url in appurls:
        print url
        response = urllib2.urlopen(url)
        data = simplejson.load(response)

        # group the departments in lists
        list1 = []
        for key, items in itertools.groupby(data, operator.itemgetter('appsrv_name')):
            list1.append(list(items))
            #print "After grouping the list by customer_name:"
            #pprint.pprint(list1)  # test
            #print "-" * 50

            # Sum of error counts by customer group
        err_list = []
        for item in list1:
            # get customer name:
            customername = item[0]['appsrv_name']
            #print  customername
            size = len(item)
            #print  size
            sum = 0
            for k in range(size):
                sum += int((item[k]['err_counts']))
            err_list.append((customername, sum))
            #print err_list
        for item in err_list:
            #print "CustomerName   %s has an total error  %d" % (item[0], item[1])
            xdata.append(item[0])
            ydata.append(item[1])
        print xdata
        print ydata

    color_list = ['#5d8aa8', '#e32636', '#efdecd', '#ffbf00', '#ff033e', '#a4c639',
                  '#b2beb5', '#8db600', '#7fffd4', '#ff007f', '#ff55a3', '#5f9ea0']
    extra_serie = {
        "tooltip": {"y_start": "", "y_end": " Errors Count"},
        "color_list": color_list
    }
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'  # container name

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('AppSrvErrs.html', data)


def demo_linewithfocuschart(request):
    """
    linewithfocuschart page
    """
    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)

    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'series 3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'series 4', 'y4': ydata4, 'extra4': extra_serie
    }
    charttype = "lineWithFocusChart"
    chartcontainer = 'linewithfocuschart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': True,
        }
    }
    return render_to_response('linewithfocuschart.html', data)


def demo_piechart(request):
    """
    pieChart page
    """
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries",
             "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    color_list = ['#5d8aa8', '#e32636', '#efdecd', '#ffbf00', '#ff033e', '#a4c639',
                  '#b2beb5', '#8db600', '#7fffd4', '#ff007f', '#ff55a3', '#5f9ea0']
    extra_serie = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "color_list": color_list
    }
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'  # container name

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('PieChart.html', data)