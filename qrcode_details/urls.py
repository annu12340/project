from django.urls import path
from . import views


urlpatterns = [
    path('', views.qrcode_func, name='qrcode'),
    path('<qrcode_id>/', views.qrcode_detail, name='qrcode-details'),

]
