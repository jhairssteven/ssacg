from django.conf                                  import settings
from django.db.models.query import QuerySet
from rest_framework                               import generics, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import SAFE_METHODS, IsAuthenticated
from rest_framework.serializers                   import Serializer
from rest_framework_simplejwt.backends            import TokenBackend

from ssacgApp.models.orders_detail                import Orders_detail
from ssacgApp.serializers.orders_detailSerializer import Orders_detailSerializer

class detailOrderView(generics.RetrieveAPIView):
    queryset = Orders_detail.objects.all()
    serializer_class = Orders_detailSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class detailOrderCreateView(generics.CreateAPIView):
    queryset = Orders_detail.objects.all()
    serializer_class = Orders_detailSerializer
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        serializer = Orders_detailSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Registro añadido exitosamente", status = status.HTTP_201_CREATED)

class detailOrderListView(generics.ListAPIView):
    serializer_class = Orders_detailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        queryset = Orders_detail.objects.filter(orders_id = self.kwargs['pk'])
        return queryset

class detailOrderUpdateView(generics.UpdateAPIView):
    queryset = Orders_detail.objects.all()
    serializer_class = Orders_detailSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().update(request, *args, **kwargs)

class detailOrderDeleteView(generics.DestroyAPIView):
    queryset = Orders_detail.objects.all()
    serializer_class = Orders_detailSerializer
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)
