from django.conf import settings
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from ssacgApp.models.clients import Clients
from ssacgApp.serializers.clientSerializer import ClientSerializer

class ClientLogInView(views.APIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *arg, **kwargs):
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token, verify=False)
        
        userObj = Clients.objects.get(email=kwargs['email'])
        # if valid_data['id_user'] != userObj['pk']:
        if not Clients.objects.filter(email=kwargs['email']).exists():
            stringResponse = {'detail': 'Unauthorized Request bro, please change user haha'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(status=status.HTTP_200_OK)