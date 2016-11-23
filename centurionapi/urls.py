from django.conf.urls import url
from django.views.generic import TemplateView
from .api import datewisedetailknwerrcntsApi,datewiseerrcntsApi

urlpatterns = [
    url(r'^dwdeknercnt$',datewisedetailknwerrcntsApi.as_view()),
    url(r'^dwercnt$',datewiseerrcntsApi.as_view()),
    url(r'^home',TemplateView.as_view(template_name="centurionapi/Home.html")),
]