from django.conf.urls import url
from django.views.generic import TemplateView
from .api import datewisedetailknwerrcntsApi,datewiseerrcntsApi
from . import views

urlpatterns = [
    url(r'^dwdeknercnt$',datewisedetailknwerrcntsApi.as_view()),
    url(r'^dwercnt$',datewiseerrcntsApi.as_view()),
    url(r'^home',TemplateView.as_view(template_name="centurionapi/Home.html")),
    url(r'^piechart$',views.demo_piechart,name='demo_piechart'),
    url(r'^jsonpiechart$',views.get_customererrpiechart,name='get_customererrpiechart'),
    url(r'^linewithfocuschart$',views.demo_linewithfocuschart,name='demo_linewithfocuschart'),
]