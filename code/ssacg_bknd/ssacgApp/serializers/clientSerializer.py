from rest_framework import serializers
from ssacgApp.models.clients import Clients

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = [
            'name',
            'email',
            'password',
            'address',
            'phone'
        ]
    
    def to_representation(self, obj):
        client = obj
        return {
            'id_user': client.id_user,
            'email': client.email,
            'phone': client.phone,
            'address': client.address,
        }

    # def create (self, **validated_data):
    #     return Client.objects.create_user(**validated_data)
