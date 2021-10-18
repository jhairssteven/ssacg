from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from ssacgApp.models.clients import Clients
from ssacgApp.serializers.clientSerializer import ClientSerializer

class ClientDetailView(generics.RetrieveAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    
    # change default field to search on get request below
    lookup_field = "id_user" 
    
    permission_classes = (IsAuthenticated,)

    def get(self, request, *arg, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['id_user'] != kwargs['id_user']:
            stringResponse = {'detail': 'Unauthorized Request bro, please change user haha'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *arg, **kwargs)