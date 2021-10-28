from django.contrib                   import admin
from django.urls                      import path
from rest_framework_simplejwt.views   import (TokenObtainPairView, TokenRefreshView)
from ssacgApp                         import views
from ssacgApp.views.productsView      import ProductsCreateView, ProductsListView, ProductsDetailView,\
                                             ProductsUpdateView, ProductsDeleteView
from ssacgApp                         import views as ssacgView

urlpatterns = [
    path('admin/',                  admin.site.urls),    
    path('login/',                  TokenObtainPairView.as_view()),    # user login
    path('refresh/',                TokenRefreshView.as_view()),    # user refresh token
    path('user/client',             views.ClientCreateView.as_view()), # client registration
    path('user/admin',              views.AdminCreateView.as_view()),  # admin registration
    path('user/byemail/<email>/',   views.EmailExistsView.as_view()),  # check email exists
    path('user/id/<int:id_user>/',  views.ClientDetailView.as_view()), # check user exists
    
    # CRUD on products table
    path('user/product/',                   ProductsCreateView.as_view()), # post
    path('user/product/show/',              ProductsListView.as_view()),   # get
    path('user/product/view/<int:pk>/',     ProductsDetailView.as_view()), # get
    path('user/product/update/<int:pk>/',   ProductsUpdateView.as_view()), # put
    path('user/product/delete/<int:pk>/',   ProductsDeleteView.as_view()),  # delete

    path('orders/create/<int:pk>/', ssacgView.OrdersCreateView.as_view()),#create one order
    path('orders/<int:user>/<int:pk>/', ssacgView.OrdersDetailView.as_view()), #shows one specific order
    path('orders/search/<int:pk>/', ssacgView.OrdersUserView.as_view()), #shows all the orders of one specific user
    path('orders/update/<int:user>/<int:pk>/', ssacgView.OrdersUpdateView.as_view()), #uptades an order
    path('orders/delete/<int:user>/<int:pk>/', ssacgView.OrdersDeleteView.as_view()), #deletes an order

    path('order_detail/create/', ssacgView.detailOrderCreateView.as_view()), #creates a detail view
    path('order_detail/getdetail/<int:pk>/', ssacgView.detailOrderView.as_view()),#gets ONE order detail
    path('order_detail/listdetail/<int:user>/<int:pk>/', ssacgView.detailOrderListView.as_view()),#gets all the pk orders
    path('order_detail/update/<int:user>/<int:pk>/', ssacgView.detailOrderUpdateView.as_view()), #updates a register
    path('order_detail/delete/<int:user>/<int:pk>/', ssacgView.detailOrderDeleteView.as_view()),#deletes a register
]
