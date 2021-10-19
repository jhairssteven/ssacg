from django.db import models


class Products(models.Model):
    id_product    = models.AutoField(primary_key = True)
    category      = models.CharField(max_length=45)
    name          = models.CharField(max_length=45)
    stock         = models.IntegerField()
    unitary_price = models.DecimalField(max_digits = 11, decimal_places = 3)
    description   = models.TextField(500)
    
    
