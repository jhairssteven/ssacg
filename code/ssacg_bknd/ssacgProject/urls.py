
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from ssacgApp import views
from ssacgApp.views.productView import ProductCreateView, ProductDeleteView
#from ssacgApp.views.productView import ProductDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    # user login    
    path('login/', TokenObtainPairView.as_view()),
    
    path('refresh/', TokenObtainPairView.as_view()),
    # client registration
    path('user/client', views.ClientCreateView.as_view()),
    # admin registration
    path('user/admin', views.AdminCreateView.as_view()),
    
    # check email exists
    path('user/byemail/<email>/', views.EmailExistsView.as_view()),
    # check user exists
    path('user/id/<int:id_user>/', views.ClientDetailView.as_view()),
    #Add product
    path('user/product' , views.ProductCreateView.as_view()),
    #Delete product
    path('user/product/remove/<int:pk>/', views.ProductDeleteView.as_view()),
    #path('user/product/remove/<str:name>/', views.ProductDeleteView.as_view()),
    #path('user/product/view/<int:id_product>', views.ProductDetailView.as_view()),


]
