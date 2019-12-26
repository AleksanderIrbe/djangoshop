from django.shortcuts import render
from django.http import HttpResponseRedirect
from ecommapp.models import Category, Brand, Product, CartItem, Cart


# Create your views here.
def base_view(request):
#	cart = Cart.objects.first()
	categories = Category.objects.all()
	products = Product.objects.all()
	context = {
		'categories':categories,
		'products': products,
#		'cart':cart,
	}
	return render(request, 'base.html', context)


def product_view(request, slug):
#	cart = Cart.objects.first()
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)

	categories = Category.objects.all()
	product = Product.objects.get(slug=slug)
	context = {
		'categories':categories,
		'product':product,
				'cart':cart
	}
	return render(request, 'product.html', context)

def category_view(request, slug):
#	cart = Cart.objects.first()
	categories = Category.objects.all()
	category = Category.objects.get(slug=slug)
	products_of_category = Product.objects.filter(category=category)
	context = {
		'categories':categories,
		'category':category,
		'products_of_category':products_of_category,
#		'cart':cart
	}
	return render(request, 'category.html', context)	

def test_view(request):
	return render(request, 'test.html')

def cart_view(request):
#	cart = Cart.objects.first()
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)

	context = {
		'cart':cart
	}
	return render(request, 'cart.html', context)

def add_to_cart_view(request, slug):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)

	product = Product.objects.get(slug=slug)
	new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
	if new_item not in cart.items.all():
		cart.items.add(new_item)
		cart.save()
		return HttpResponseRedirect('/cart/')

def remove_from_cart_view(request, slug):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)
	product = Product.objects.get(slug=slug)
	new_item, _ = CartItem.objects.get_or_create(product=product)
	
	if new_item not in cart.items.all():
		cart.items.add(new_item)
		cart.save()
		return HttpResponseRedirect('/cart/')
