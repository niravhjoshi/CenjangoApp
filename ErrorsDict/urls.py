from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.http import request

urlpatterns = [
    url(r'^errordictshow', views.errorsdict_show,name='errordictshow'),
    url(r'^errordictadd', views.errorsdict_add,name='errordictadd'),
    url(r'^errordictupdate',views.errorsdict_update,name='errordictupdt'),
    url(r'^SingleError/$', views.Single_errors_graph2, name='SingleErrName'),
    url(r'^singlerrorbymonth/$',views.Single_errors_graph2_ViewByMonth,name='SingleErrorbyMonth'),
    url(r'^singlerrorbycust/$', views.Single_errors_graph2_viewByCustomer, name='SingleErrorbyCust'),
    url(r'^singlerrorbydates/$', views.Single_errors_graph2_viewByDates, name='SingleErrorbyDates'),
    url(r'^errjsonpiechart$',views.errorsdetPie,name='errors_pie'),

    #url(r'^SingleError/(?P<any>\w+)/$',views.Single_errors_graph1,name='SingleErrCnt'),
    #url(r'^SingleError/(?P<q>\w+)/$',views.Single_errors_graph1,{'title':'Single Errors Chart','sidebar_items':'Charts Pivot'},name="SingleErrCnt"),
    #url(r'^SingleError/$',views.Single_errors_graph1,{'title':'Single Errors Chart','sidebar_items':'Charts Pivot'},name="SingleErrCnt"),

]