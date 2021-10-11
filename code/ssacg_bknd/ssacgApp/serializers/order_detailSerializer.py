from rest_framework import serializers
from ssacgApp.models.order_detail import Order_detail

class Order_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order_detail
        fields = ['id_product','id_order' 'product_quantity', 'total']