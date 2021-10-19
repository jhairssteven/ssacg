from ssacgApp.models.products import Products
from rest_framework import serializers
from ssacgApp.models.admins import Admins

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields = ['pk','name', 'category', 'unitary_price', 'stock', 'description']
    
    def to_representation(self, obj):
        admin = Admins.objects.get(id=obj.admin)
        product = Products.objects.get(id_product=obj.id_product)
        
        return {
            'id_product'    : product.id_product,
            'name'          : product.name,
            'category'      : product.category,
            'unitary_price' : product.unitary_price,
            'stock'         : product.stock,
            'description'   : product.description,
            'admin'  :{
                'id_user'  : admin.id_user,
                'name'      : admin.name,
                'email'     : admin.email
            }
        }