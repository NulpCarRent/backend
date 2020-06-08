from django.urls import path
from api.views import AutoViewSet, ClientViewSet, RequestViewSet, FineViewSet
from rest_framework.routers import SimpleRouter
from django.urls import include

router = SimpleRouter()

router.register('autos', AutoViewSet, basename='auto')
router.register('clients', ClientViewSet, basename='client')
router.register('requests', RequestViewSet, basename='request')
router.register('fines', FineViewSet, basename='fine')

urlpatterns = [
    path('', include(router.urls))
]
