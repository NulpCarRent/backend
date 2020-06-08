from django.shortcuts import render
from rest_framework import viewsets
from api.models import Auto, Client, Request, Fine
from api.serializers import AutoSerializer, ClientSerializer, RequestSerializer, FineSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer