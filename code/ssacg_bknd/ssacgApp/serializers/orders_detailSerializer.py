from rest_framework import serializers
from ssacgApp.models.orders_detail import Orders_detail
from ssacgApp.models.products import Products
from ssacgApp.models.orders import Orders

class Orders_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Orders_detail
        fields = [
            'id_product',
            'id_order',
            'product_quantity',
            'total']
    def to_representation(self, obj):
        orders = Orders.objects.get(id = obj.order_id)
        products = Products.objects.get(id_product  = obj.product_id)
        detail = Orders_detail.objects.get(id_order_detail = obj.id_order_detail)
        return {
            'id': detail.id_order_detail,
            'Cantidad': detail.product_quantity,
            'products': {
                'id_product'    : products.id_product,
                'name'          : products.name,
                'category'      : products.category,
                'unitary_price' : products.unitary_price,
                'stock'         : products.stock,
                'description'   : products.description  
            },
            'Order':{ 
                'id': orders.order_id,
            
            }
        }

        return super().to_representation(instance)