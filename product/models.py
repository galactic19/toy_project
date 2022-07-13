from django.db import models
from django.urls import reverse


class Thumb(models.Model):
    ''' 썸네일 이미지를 관리 '''
    name = models.CharField(max_length=100, db_index=True, help_text='등록하는 이미지의 모델명을 입력하세요')
    front_image = models.ImageField(upload_to='thumb/%Y/%m/%d', null=True, default='none.png')
    left_image = models.ImageField(upload_to='thumb/%Y/%m/%d', blank=True)
    back_image = models.ImageField(upload_to='thumb/%Y/%m/%d', blank=True)
    right_image = models.ImageField(upload_to='thumb/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name_plural = '상품 등록 관리'
    
    def __str__(self):
        return self.name
    
    def prd_price(self):
        return self.thumb.price
    prd_price.short_description='출고가'
    
    def manufacturer_list(self):
        return self.thumb.manufacturer.name
    manufacturer_list.short_description = '제조사'
    
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    image = models.ImageField(upload_to='manufacturer', blank=True, help_text='제조사 로고이미지')
    homepage = models.URLField(blank=True, help_text='제조사 홈페이지')

    class Meta:
        ordering = ['name',]
        verbose_name_plural = '제조사 등록/관리'
        
    def __str__(self):
        return self.name


class ProductVolumeOptions(models.Model):
    ''' 
        단말기 용량을 가진다.
        단말기 용량별 색상과 출고가는 달라질 수 있다.
        통신사별로도 출시색상과 용량이 달라질 수 있다.
    '''
    name = models.CharField(max_length=30)
    volume = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField(default=0)
        

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    model_name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    price = models.PositiveSmallIntegerField()
    thumbnail = models.OneToOneField(Thumb, on_delete=models.CASCADE, related_name='thumb')
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL, related_name='product')
    volume = models.ForeignKey(ProductVolumeOptions, null=True, on_delete=models.CASCADE, related_name='productvolume')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at', 'name']
        verbose_name_plural = '상품/모델 관리'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"slug": self.slug})
    