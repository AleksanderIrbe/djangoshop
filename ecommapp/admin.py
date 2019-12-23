from django.contrib import admin
from ecommapp.models import Category, Brand, Product

#admin.site.register(Category)
admin.site.register(Brand)
#admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",)}




# Register your models here.
