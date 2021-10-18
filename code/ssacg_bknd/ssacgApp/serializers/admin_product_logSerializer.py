from rest_framework import serializers
from ssacgApp.models.admin_product_log import Admin_product_log

class Admin_product_logSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_product_log
        field = [
            'id_product',
            'id_admin',
            'operation'
        ]