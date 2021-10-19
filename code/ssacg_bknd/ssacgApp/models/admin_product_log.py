from django.db import models
from .products import Products
from .admins import Admins

class Admin_product_log(models.Model):
    id_product_log = models.BigAutoField(primary_key=True)
    operation = models.CharField('CRUD operation type', max_length = 1, default='r') # 4 posible values ('c', 'r', 'u' and 'd')
    
    product = models.ForeignKey(Products, related_name= "product_admin_log", null = True, blank = True, on_delete = models.CASCADE)
    admin = models.ForeignKey(Admins, related_name= "admin_log_admin", null = True, blank = True, on_delete = models.CASCADE)

    