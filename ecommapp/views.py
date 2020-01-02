from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, JsonResponse
from ecommapp.models import Category, Brand, Product, CartItem, Cart
from decimal import Decimal


# Create your views here.
def base_view(request):
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
	products = Product.objects.all()
	context = {
		'categories':categories,
		'products': products,
		'cart':cart,
	}
	return render(request, 'base.html', context)


def product_view(request, product_slug):
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
	product = Product.objects.get(slug=product_slug)
	context = {
		'categories':categories,
		'product':product,
		'cart':cart
	}
	return render(request, 'product.html', context)

def category_view(request, category_slug):
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
	category = Category.objects.get(slug=category_slug)
	products_of_category = Product.objects.filter(category=category)
	context = {
		'categories':categories,
		'category':category,
		'products_of_category':products_of_category,
		'cart':cart
	}
	return render(request, 'category.html', context)	

def test_view(request):
	return render(request, 'test.html')

def cart_view(request):
#	cart = Cart.objects.first()
	categories = Category.objects.all()
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
		'categories':categories,
		'cart':cart
	}
	return render(request, 'cart.html', context)

def add_to_cart_view(request):
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

	product_slug = request.GET.get('product_slug')
	product = Product.objects.get(slug=product_slug)
	# new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
	# if new_item not in cart.items.all():
	# 	cart.items.add(new_item)
	# 	cart.save()
	# 	return HttpResponseRedirect('/cart/')
	cart.add_to_cart(product.slug)
	#return HttpResponseRedirect(reverse('cart'))
	return JsonResponse({'cart_total':cart.items.count()})

def remove_from_cart_view(request):
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
	product_slug = request.GET.get('product_slug')
	product = Product.objects.get(slug=product_slug)
	# for cart_item in cart.items.all():
	# 	if cart_item.product == product:
	# 		cart.items.remove(cart_item)
	# 		cart.save()
	# 		return HttpResponseRedirect('/cart/')
	cart.remove_from_cart(product.slug)
#	return HttpResponseRedirect(reverse('cart'))
	return JsonResponse({'cart_total':cart.items.count()})


def change_item_qty(request):
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

	qty = request.GET.get('qty')		
	item_id = request.GET.get('item_id')
	cart_item = CartItem.objects.get(id=int(item_id))
	cart_item.qty = int(qty)
	cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
	cart_item.save()
	return JsonResponse({'cart_total':cart.items.count(), 'item_total': cart_item.item_total})

