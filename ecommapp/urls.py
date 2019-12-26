
from django.urls import path

from django.conf.urls import url, include
from ecommapp.views import *


urlpatterns = [
	path('', base_view, name='base'),
	path('category/<str:slug>/', category_view, name='category_detail'),
	path('product/<str:slug>/', product_view, name='product_detail'),
	path('add_to_cart/<str:slug>/', add_to_cart_view, name='add_to_cart'),
	path('cart/', cart_view, name='cart'),



	path('test/', test_view, name='test'),
    
]