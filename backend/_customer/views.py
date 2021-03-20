from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import routers

from backend._customer import models
from backend._customer import serializers


class CustomerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing website objects.
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = [permissions.AllowAny]


customer_router = routers.SimpleRouter()
customer_router.register('', CustomerViewSet, basename='customers')
