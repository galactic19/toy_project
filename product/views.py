from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Thumb


def product_list(request):
    return HttpResponse('상품 리스트')