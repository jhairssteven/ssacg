from django.conf                                  import settings
from django.shortcuts                             import render
from rest_framework                               import generics, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import IsAuthenticated
from rest_framework_simplejwt.backends            import TokenBackend
from ssacgApp                                     import views

from ssacgApp.models.products                     import Products
from ssacgApp.serializers.productsSerializer      import ProductsSerializer

#create a new product: ya
class ProductsCreateView(generics.CreateAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Agregado", status=status.HTTP_201_CREATED)

#list all the products: ya, pero desordenada
class ProductsListView(generics.ListAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    permission_classes = (IsAuthenticated,)
    

#check for a single product: ya
class ProductsDetailView(generics.RetrieveAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args, **kwargs):

        return super().get(request,*args, **kwargs)

#update products: ya
class ProductsUpdateView(generics.RetrieveUpdateAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        
        return super().update(request, *args, **kwargs)

#delete products
class ProductsDeleteView(generics.RetrieveDestroyAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    permission_classes = (IsAuthenticated,)

    #como se puede eliminar solo si el usuario tiene los permisos ?
    """def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['id_user'] != kwargs['id_user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)"""