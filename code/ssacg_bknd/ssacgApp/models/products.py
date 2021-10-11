from django.db import models
from admins import Admins

class Products(models.Model):
    id_product = models.AutoField(primary_key = True)
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    stock= models.IntegerField()
    unitary_price = models.DecimalField()
    description = models.TextField(500)
    admin = models.ForeignKey(Admins, null = True, blank = True, on_delete= models.CASCADE)