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

    def __init__(self, *args, **kwargs):
        super(datewiseerrcntsSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.query_params.get('fields'):
            fields = request.query_params.get('fields')
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing  = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)

