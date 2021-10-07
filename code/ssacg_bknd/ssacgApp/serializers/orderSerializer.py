from ssacgApp.models.order import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['fecha' 'id_producto' 'cantidad_producto' 'estado']
