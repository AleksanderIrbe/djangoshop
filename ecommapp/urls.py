
from django.urls import path

from django.conf.urls import url, include
from ecommapp.views import *


urlpatterns = [
	path('', base_view, name='base'),
	path('category/<str:slug>/', category_view, name='category_detail'),
	path('product/<str:slug>/', product_view, name='product_detail'),
	path('test/', test_view, name='test'),
    
]