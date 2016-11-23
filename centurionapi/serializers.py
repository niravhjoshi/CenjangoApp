from rest_framework import serializers
#This will convert our model class from python object to serializer (json) for Angular.
from .models import datewisedetailknownerrcounts,datewiseerrcounts

class datewisedetailknownerrcntsSerializer(serializers.ModelSerializer):

    class Meta:
        model = datewisedetailknownerrcounts
        fields = '__all__'

class datewiseerrcntsSerializer(serializers.ModelSerializer):

    class Meta:
        model = datewiseerrcounts
        fields = '__all__'