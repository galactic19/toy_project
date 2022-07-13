from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    description = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d', blank=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    # sequence = models. 별도의 메서드를 생성해야 할듯.
    
    class Meta:
        ordering = ['name', 'parent']
        verbose_name_plural = '카테고리'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category:category_list', kwargs={"slug":self.slug})