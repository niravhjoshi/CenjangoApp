from django.conf.urls import url
from django.views.generic import TemplateView
from .api import datewisedetailknwerrcntsApi,datewiseerrcntsApi
from . import views
from .decorators import add_source_code_and_doc

urlpatterns = [
    url(r'^dwdeknercnt$',datewisedetailknwerrcntsApi.as_view()),
    url(r'^dwercnt$',datewiseerrcntsApi.as_view()),
    url(r'^home',views.home,name='home'),
    url(r'^about',views.about,name='about'),
    url(r'^piechart$',views.demo_piechart,name='demo_piechart'),
    url(r'^jsonpiechart$',views.get_customererrpiechart,name='get_customererrpiechart'),
    url(r'^linewithfocuschart$',views.demo_linewithfocuschart,name='demo_linewithfocuschart'),
    url(r'^AppSrvErrs$',views.get_appsrvnameerrcntschart,name='AppSrvErrs'),
    url(r'^NewChart$',views.month_appsrv_cntsit,
        {'title':'Line Chart',
         'sidebar_items':'Charts w/ RawQuerySet',},
        name='NewChart'),
    url(r'^PivotChart$',views.month_appsrv_pivot,
        {'title':'Pivot Chart',
         'sidebar_items':'Charts Pivot',},
        name='PivotChart'),
]