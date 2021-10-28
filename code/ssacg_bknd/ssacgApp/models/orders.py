from django.db import models
from .clients import Clients

class Orders (models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, related_name='Client',null=True, blank=True,on_delete= models.CASCADE)