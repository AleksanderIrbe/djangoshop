
from django.urls import path

from django.conf.urls import url, include
from ecommapp.views import *


urlpatterns = [
	path('', base_view, name='base'),
	path('category/<str:category_slug>/', category_view, name='category_detail'),
	path('product/<str:product_slug>/', product_view, name='product_detail'),
	path('add_to_cart/', add_to_cart_view, name='add_to_cart'),
	path('remove_from_cart/', remove_from_cart_view, name = 'remove_from_cart'),
	path('change_item_qty/', change_item_qty, name='change_item_qty'),
	path('cart/', cart_view, name='cart'),



	path('test/', test_view, name='test'),
    
]