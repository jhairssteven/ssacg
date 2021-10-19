"""ssacgProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib                   import admin
from django.urls                      import path
from rest_framework_simplejwt.views   import (TokenObtainPairView, TokenRefreshView)
from ssacgApp                         import views
from ssacgApp.views.productsView      import ProductsCreateView, ProductsListView, ProductsDetailView,\
                                             ProductsUpdateView, ProductsDeleteView

urlpatterns = [
    path('admin/',                  admin.site.urls),    
    path('login/',                  TokenObtainPairView.as_view()),    # user login
    path('refresh/',                TokenObtainPairView.as_view()),    # user refresh token
    path('user/client',             views.ClientCreateView.as_view()), # client registration
    path('user/admin',              views.AdminCreateView.as_view()),  # admin registration
    path('user/byemail/<email>/',   views.EmailExistsView.as_view()),  # check email exists
    path('user/id/<int:id_user>/',  views.ClientDetailView.as_view()), # check user exists
    
    # CRUD on products table
    path('user/product/',                   ProductsCreateView.as_view()), # post
    path('user/product/show/',              ProductsListView.as_view()),   # get
    path('user/product/view/<int:pk>/',     ProductsDetailView.as_view()), # get
    path('user/product/update/<int:pk>/',   ProductsUpdateView.as_view()), # put
    path('user/product/delete/<int:pk>/',   ProductsDeleteView.as_view())  # delete
]
