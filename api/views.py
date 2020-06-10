from django.shortcuts import render
from rest_framework import viewsets
from api.models import Auto, Client, Request, Fine
from api.serializers import AutoSerializer, ClientSerializer, RequestSerializer, FineSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'available']

    def get_queryset(self):
        queryset = super().get_queryset()
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')

        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        return queryset

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
