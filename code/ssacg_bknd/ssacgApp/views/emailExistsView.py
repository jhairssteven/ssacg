from django.conf import settings
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from ssacgApp.models.users import Users
from ssacgApp.serializers.adminSerializer import AdminSerializer

class EmailExistsView(views.APIView):
    queryset = Users.objects.all()
    serializer_class = AdminSerializer

    def get(self, request, *arg, **kwargs):
        if not Users.objects.filter(email=kwargs['email']).exists():
            stringResponse = {'detail': 'Email not found'}
            return Response(stringResponse, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Detail': 'Email does indeed exists'}, status=status.HTTP_200_OK)