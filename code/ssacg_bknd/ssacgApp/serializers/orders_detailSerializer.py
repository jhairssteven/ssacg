from rest_framework import serializers
from ssacgApp.models.orders_detail import Orders_detail

class Orders_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Orders_detail
        fields = [
            'id_product',
            'id_order',
            'product_quantity',
            'total']