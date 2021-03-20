from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import routers

from backend._order import models
from backend._order import serializers


class OrderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing website objects.
    """
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.AllowAny]


order_router = routers.SimpleRouter()
order_router.register('', OrderViewSet, basename='orders')
