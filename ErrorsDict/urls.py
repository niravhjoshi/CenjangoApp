from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^errordictshow', views.errorsdict_show,name='errordictshow'),
    url(r'^errordictadd', views.errorsdict_add,name='errordictadd'),
    url(r'^errordictupdate',views.errorsdict_update,name='errordictupdt'),

]