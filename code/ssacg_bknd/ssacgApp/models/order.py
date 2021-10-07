from django.db import models
from .client import Client

class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name="cliente_account", on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    
    id_producto = models.CharField('Id_Producto', max_length=100)
    cantidad_producto = models.IntegerField(default=1)
    estado = models.BooleanField(default=False)