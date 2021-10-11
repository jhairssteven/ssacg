from rest_framework import serializers
from ssacgApp.models.admins import Admins

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = [
            'name',
            'email', 
            'password'
        ]

    # def create (self, **validated_data):
    #     return Admin.objects.create_user(**validated_data)