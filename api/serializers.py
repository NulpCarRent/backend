from rest_framework import serializers
from api.models import Auto, Client, Request

class AutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Auto
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Request
        fields = '__all__'

