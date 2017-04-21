from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.http import request

urlpatterns = [
    url(r'^errordictshow', views.errorsdict_show,name='errordictshow'),
    url(r'^errordictadd', views.errorsdict_add,name='errordictadd'),
    url(r'^errordictupdate',views.errorsdict_update,name='errordictupdt'),
    url(r'^SingleError/$', views.Single_errors_graph2, name='SingleErrName'),
    #url(r'^SingleError/(?P<any>\w+)/$',views.Single_errors_graph1,name='SingleErrCnt'),
    #url(r'^SingleError/(?P<q>\w+)/$',views.Single_errors_graph1,{'title':'Single Errors Chart','sidebar_items':'Charts Pivot'},name="SingleErrCnt"),
    #url(r'^SingleError/$',views.Single_errors_graph1,{'title':'Single Errors Chart','sidebar_items':'Charts Pivot'},name="SingleErrCnt"),

]