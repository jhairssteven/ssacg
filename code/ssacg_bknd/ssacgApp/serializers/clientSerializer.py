from rest_framework import serializers
from ssacgApp.models.client import Client
from ssacgApp.models.order import Order
from ssacgApp.serializers.orderSerializer import OrderSerializer


class ClientSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Client
        fields = [
            'id_cliente',
            'nombre',
            'address',
            'phoneNumber',
            'password',
            'email',
            'last_connection',
            'order']
    
    def create(self, validated_data):
        orderData = validated_data.pop('order')
        clientInstance = Client.objects.create(**validated_data)
        Order.objects.create(client=clientInstance, **orderData)
        return clientInstance

    def to_representation(self, obj):
        client = Client.objects.get(id=obj.id)
        order = Order.objects.get(client=obj.id)
        return {
            'id_cliente': client.id_cliente,
            'nombre': client.nombre,
            'address': client.address,
            'phoneNumber': client.phoneNumber,
            'password': client.password,
            'email': client.email,
            'last_connection': client.last_connection,

            'order': {
                'id_order': order.id_order,
                'client': order.client,
                'fecha': order.fecha,
                'id_producto': order.id_producto,
                'cantidad_producto': order.cantidad_producto,
                'estado': order.estado
            }
        }

