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


def product_view(request, slug):
	categories = Category.objects.all()
	product = Product.objects.get(slug=slug)
	context = {
		'categories':categories,
		'product':product
	}
	return render(request, 'product.html', context)

def category_view(request, slug):
	categories = Category.objects.all()
	category = Category.objects.get(slug=slug)
	products_of_category = Product.objects.filter(category=category)
	context = {
		'categories':categories,
		'category':category,
		'products_of_category':products_of_category
	}
	return render(request, 'category.html', context)	

def test_view(request):
	return render(request, 'test.html')