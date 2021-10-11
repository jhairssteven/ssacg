from ssacgApp.models.products import Products
from rest_framework import serializers
from ssacgApp.models.admins import Admins

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields = ['name', 'category', 'unitary_price', 'stock', 'description']
    def to_representation(self, obj):
        admin = Admins.objects.get(id=obj.admin)
        product = Products.objects.get(id=obj.id)
        return {
            'id_product'    : product.id_product,
            'name'          : product.name,
            'category'      : product.category,
            'unitary_price' : product.unitary_price,
            'stock'         : product.stock,
            'description'   : product.description,
            'admin'  :{
                'id_admin'  : admin.id_admin,
                'name'      : admin.name,
                'email'     : admin.email
            }
        }