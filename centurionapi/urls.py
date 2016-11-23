from django.conf.urls import url

from .api import datewisedetailknwerrcntsApi,datewiseerrcntsApi

urlpatterns = [
    url(r'^dwdeknercnt$',datewisedetailknwerrcntsApi.as_view()),
    url(r'^dwercnt$',datewiseerrcntsApi.as_view())
]