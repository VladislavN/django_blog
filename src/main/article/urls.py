from django.contrib import admin
from django.urls import path, include
import article.views

urlpatterns = [
    path('1/', article.views.basic_one),
    path('2/', article.views.template_two),
    path('3/', article.views.template_three_simple),
]
