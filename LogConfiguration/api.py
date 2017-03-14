from rest_framework.generics import ListAPIView

from .serializers import CustomerProdLogsLocaSerializer
from .models import CustomerProdLogsLoca


class CustomerProdLogsLocaApi(ListAPIView):
    queryset = CustomerProdLogsLoca.objects.all()
    serializer_class = CustomerProdLogsLocaSerializer


    def get_queryset(self):
        'allow filter to apply on api return result by customer name attribute'
        queryset = CustomerProdLogsLoca.objects.all()
        cust_name = self.request.query_params.get('cust_name',None)
        srv1_name = self.request.query_params.get('srv1_name_dir',None)
        srv2_name = self.request.query_params.get('srv2_name_dir',None)
        srv98_name = self.request.query_params.get('srv98_name_dir', None)
        srv99_name = self.request.query_params.get('srv99_name_dir', None)
        appsrv_tools_logpath = self.request.query_params.get('appsrv_tools_logpath', None)
        appsrv_localws_logpath = self.request.query_params.get('appsrv_localws_logpath',None)
        log_monitor = self.request.query_params.get('log_monitor',None)
        if cust_name is not None:
            queryset = queryset.filter(cust_name=cust_name)
        if srv1_name is not None:
            queryset = queryset.filter(srv2_name_dir=srv1_name)
        if srv2_name is not None:
            queryset = queryset.filter(srv2_name_dir=srv2_name)
        if srv98_name is not None:
            queryset = queryset.filter(srv98_name_dir=srv98_name)
        if srv99_name is not None:
            queryset = queryset.filter(srv99_name_dir=srv99_name)
        if appsrv_tools_logpath is not None:
            queryset = queryset.filter(appsrv_tools_logpath=appsrv_tools_logpath)
        if appsrv_localws_logpath is not None:
            queryset = queryset.filter(appsrv_localws_logpath=appsrv_localws_logpath)
        if log_monitor is not None:
            queryset = queryset.filter(log_monitor=log_monitor)

        return queryset