from django.db import models
from .orders import Orders
from .products import Products
class Order_detail (models.Model):
    id_order_detail = models.BigAutoField(primary_key=True)
    id_product = models.ForeignKey(Products, related_name = 'order_detail_products', on_delete= models.CASCADE)
    id_order =models.ForeignKey(Orders, related_name = 'order_detail', on_delete= models.CASCADE)
    product_quantity = models.IntegerField(default = 1 )
    total = models.DecimalField(max_digits =11, decimal_places=3)
