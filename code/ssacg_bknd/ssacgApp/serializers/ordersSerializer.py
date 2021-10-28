from rest_framework import serializers
from ssacgApp.models.orders import Orders
from ssacgApp.models.clients import Clients
from ssacgApp.models.users import Users

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['client']

        def to_representation(self, obj):
            order = Orders.objects.get(id = obj.id)
            client = Clients.objects.get(users_ptr_id = obj.users_ptr_id)
            user = Users.objects.get(id_user = obj.id_user)

            return {
                'id' : order.id,
                'client': {
                    'id_user': client.users_ptr_id,
                    'name': user.name,
                    'email': user.email,
                    'phone': client.phone,
                    'address': client.address,
                }
            }