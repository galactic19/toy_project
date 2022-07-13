from django.db import models
from django.urls import reverse


class Thumb(models.Model):
    ''' 썸네일 이미지를 관리 '''
    front_image = models.ImageField(upload_to='thumb/%Y/%m/%d', null=True, default='none.png')
    left_image = models.ImageField(upload_to='thumb/%Y/%m/%d', blank=True)
    back_image = models.ImageField(upload_to='thumb/%Y/%m/%d', blank=True)
    right_image = models.ImageField(upload_to='thumb/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name_plural = '썸네일 이미지'
    
    def __str__(self):
        return self.front_image.url
        

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    model_name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    price = models.PositiveSmallIntegerField()
    thumbnail = models.ForeignKey(Thumb, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at', 'name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"slug": self.slug})
    