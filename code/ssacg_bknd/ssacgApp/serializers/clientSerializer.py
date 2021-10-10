from rest_framework import serializers
from ssacgApp.models.client import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'name',
            'email',
            'password',
            'address',
            'phone'
        ]