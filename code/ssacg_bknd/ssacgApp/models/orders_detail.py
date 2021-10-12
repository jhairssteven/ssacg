from django.db import models
from .orders import Orders
from .products import Products

class Orders_detail (models.Model):
    id_order_detail  = models.BigAutoField(primary_key=True)
    product_quantity = models.IntegerField(default = 1 )
    total            = models.DecimalField(max_digits =11, decimal_places=3)

    product          = models.ForeignKey(Products, related_name = 'order_detail_products', null = True, blank = True,  on_delete= models.CASCADE)
    order            = models.ForeignKey(Orders, related_name = 'order_order_detail', null = True, blank = True, on_delete= models.CASCADE)
