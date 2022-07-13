from django.urls import path
from . import views

app_name = 'plan'

urlpatterns = [
    path('', views.plan_list, name="plan_list"),
]
