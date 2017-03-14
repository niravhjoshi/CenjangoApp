from rest_framework import serializers
from .models import CustomerProdLogsLoca

class CustomerProdLogsLocaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerProdLogsLoca
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerProdLogsLocaSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.query_params.get('fields'):
            fields = request.query_params.get('fields')
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing  = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)

