from django.contrib import admin
from ecommapp.models import *

admin.site.register(Brand)
admin.site.register(CartItem)
admin.site.register(Cart)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",)}




# Register your models here.
