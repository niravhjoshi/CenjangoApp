from rest_framework.generics import ListAPIView

from .serializers import datewisedetailknownerrcntsSerializer,datewiseerrcntsSerializer
from .models import datewiseerrcounts,datewisedetailknownerrcounts


class datewisedetailknwerrcntsApi(ListAPIView):
    queryset = datewisedetailknownerrcounts.objects.all()
    serializer_class = datewisedetailknownerrcntsSerializer


class datewiseerrcntsApi(ListAPIView):
    queryset = datewiseerrcounts.objects.all()
    serializer_class = datewiseerrcntsSerializer