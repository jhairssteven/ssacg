from rest_framework import serializers
from ssacgApp.models.admin import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = [
            'name',
            'email', 
            'password'
        ]

    # def create (self, **validated_data):
    #     return Admin.objects.create_user(**validated_data)