from django.shortcuts import render
from django.http import HttpResponse
from ecommapp.models import Category, Brand, Product


# Create your views here.
def base_view(request):
	categories = Category.objects.all()
	products = Product.objects.all()
	context = {
		'categories':categories,
		'products': products
	}
	return render(request, 'base.html', context)