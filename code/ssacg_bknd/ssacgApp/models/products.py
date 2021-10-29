from django.db import models
from django.core import validators


class Products(models.Model):
    id_product    = models.AutoField(primary_key = True)
    img_src       = models.CharField(max_length=65534, default="Sin imágen")
    category      = models.CharField(max_length=45)
    name          = models.CharField(max_length=45)
    stock         = models.IntegerField(validators=[validators.MinValueValidator(1, message="invalid stock input")])
    unitary_price = models.DecimalField(max_digits = 11, decimal_places = 3, validators=[validators.MinValueValidator(0.000, message="invalid price input")])
    description   = models.TextField(500)
    
    
