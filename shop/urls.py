from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_page, name='shop'),
    path('product/<product_id>', views.product_details, name='product-details'),
    path('orders', views.my_orders, name='my_orders'),
    path('maps', views.maps, name='maps'),
    path('checkout', views.checkout, name='checkout'),
    path('successful', views.successful, name='successful'),

]
