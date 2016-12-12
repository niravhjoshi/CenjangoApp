from rest_framework.generics import ListAPIView

from .serializers import datewisedetailknownerrcntsSerializer,datewiseerrcntsSerializer
from .models import datewiseerrcounts,datewisedetailknownerrcounts


class datewisedetailknwerrcntsApi(ListAPIView):
    queryset = datewisedetailknownerrcounts.objects.all()
    serializer_class = datewisedetailknownerrcntsSerializer


class datewiseerrcntsApi(ListAPIView):
    queryset = datewiseerrcounts.objects.all()
    serializer_class = datewiseerrcntsSerializer

    def get_queryset(self):
        'allow filter to apply on api return result by customer name attribute'
        queryset = datewiseerrcounts.objects.all()
        cust_name = self.request.query_params.get('cust_name',None)
        month_name = self.request.query_params.get('month_name',None)
        appsrv_name = self.request.query_params.get('appsrv_name',None)
        date_stamp = self.request.query_params.get('date_stamp',None)
        if cust_name is not None:
            queryset = queryset.filter(cust_name=cust_name)
        if month_name is not None:
            queryset = queryset.filter(month_name=month_name)
        if appsrv_name is not None:
            queryset = queryset.filter(appsrv_name=appsrv_name)
        if date_stamp is not None:
            queryset = queryset.filter(date_stamp=date_stamp)

        return queryset