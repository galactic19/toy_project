from django.contrib import admin
from .models import Product, Thumb, Manufacturer, ProductVolumeOptions


class ProductStackedInline(admin.StackedInline):
    model = Product
    verbose_name = '모델등록'
    prepopulated_fields = {"slug":('name',)}


@admin.register(Thumb)
class ThumbAdmin(admin.ModelAdmin):
    inlines = (ProductStackedInline, )
    list_display = ['id', 'name', 'manufacturer_list', 'model_volume', 'prd_price', 'front_image']
    list_display_links = ['id', 'name']
    verbose_name = '상품 관리'


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    
@admin.register(ProductVolumeOptions)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'volume', 'price']
    verbose_name = '모델 용량 및 옵션 관리'