from rest_framework import serializers
from api.models import Auto, Client, Request, Fine

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

    def create(self, validated_data):
        auto = validated_data.get('auto')
        client = validated_data.get('renter')

        auto.renter = client
        auto.save()

        return super().create(validated_data)

class FineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fine
        fields = '__all__'
