from ssacgApp.models.products import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields = ['pk', 'name', 'img_src', 'category', 'unitary_price', 'stock', 'description']
    
    def to_representation(self, obj):
        products = Products.objects.get(id_product=obj.id_product)
        
        return {
            'id_product'    : products.id_product,
            'img_src'       : products.img_src,
            'name'          : products.name,
            'category'      : products.category,
            'unitary_price' : products.unitary_price,
            'stock'         : products.stock,
            'description'   : products.description            
        }
    
