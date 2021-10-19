from django.conf    import settings
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from ssacgApp import views


from ssacgApp.models.products import Products
from ssacgApp.serializers import productsSerializer
from ssacgApp.serializers.productsSerializer import ProductsSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Agregado", status=status.HTTP_201_CREATED)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args, **kwargs):

        return super().get(request,*args, **kwargs)

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self,request,*args,**kwargs):
        token   = request.META.get('HTTP_AUTHORIZATION')[7:]#Generador de tockens
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)


        return super().destroy(request,*args,**kwargs)
