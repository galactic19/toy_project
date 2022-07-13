from django.shortcuts import render
from django.http import HttpResponse


def plan_list(request):
    return HttpResponse('요금제 리스트')