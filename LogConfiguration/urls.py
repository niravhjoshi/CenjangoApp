from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from .api import CustomerProdLogsLocaApi

urlpatterns = [
    url(r'^customeradd', views.customer_add,name='customeradd'),
    url(r'^errorsdict', views.Errors_Dict,name='errorsdict'),
    url(r'^LogLocation',views.NewLog_File,name='LogLocation'),
    url(r'^CustomerLoglocationapi$',CustomerProdLogsLocaApi.as_view()),
]