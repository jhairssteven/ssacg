from django.conf                                  import settings
from django.shortcuts                             import render
from rest_framework                               import generics, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import IsAuthenticated
from rest_framework_simplejwt.backends            import TokenBackend
from ssacgApp                                     import views

from ssacgApp.models.products                     import Products
from ssacgApp.serializers.productsSerializer      import ProductsSerializer

class ProductsCreateView(generics.CreateAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        newProduct = serializer.save()
        
        return Response(serializer.to_representation(newProduct), status=status.HTTP_201_CREATED)

#list all the products: ya, pero desordenada
class ProductsListView(generics.ListAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    # permission_classes = (IsAuthenticated,)

    

class ProductsDetailView(generics.RetrieveAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    # permission_classes = (IsAuthenticated,)

    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductsUpdateView(generics.RetrieveUpdateAPIView):
    queryset           = Products.objects.all()
    serializer_class   = ProductsSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        
        return super().update(request, *args, **kwargs)

class ProductsDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self,request,*args,**kwargs):
        token   = request.META.get('HTTP_AUTHORIZATION')[7:] # Generador de tokens
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        return super().destroy(request,*args,**kwargs)