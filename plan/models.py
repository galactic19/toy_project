from django.db import models
from django.urls import reverse


class Telecom(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    image = models.ImageField(upload_to='telecom', blank=True, verbose_name='통신사 로고이미지')
    homepage_url = models.URLField(blank=True, verbose_name='통신사 홈페이지')
    

class Ltetype(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100, blank=True)


class Plan(models.Model):
    telecom = models.ForeignKey(Telecom, on_delete=models.CASCADE, related_name='telecom')
    ltetype = models.ForeignKey(Ltetype, null=True, on_delete=models.SET_NULL, related_name='ltetype')
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    price = models.PositiveSmallIntegerField()
    discount_money = models.PositiveSmallIntegerField()
    discount_add_money = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at', '-updated_at', 'name']

    def __str__(self):
        return self.name
