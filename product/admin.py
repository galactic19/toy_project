from django.contrib import admin
from .models import Product, Thumb, Manufacturer


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'model_name', 'price']
#     prepopulated_fields = {'slug':('name',)}
#     verbose_name = '상품 등록'


class ProductStackedInline(admin.StackedInline):
    model = Product
    verbose_name = '모델등록'


@admin.register(Thumb)
class ThumbAdmin(admin.ModelAdmin):
    inlines = (ProductStackedInline, )
    list_display = ['id', 'name', 'manufacturer_list', 'prd_price', 'front_image']
    list_display_links = ['id', 'name']
    verbose_name = '상품 관리'


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']