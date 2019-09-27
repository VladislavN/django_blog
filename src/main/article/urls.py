import re
from django.contrib import admin
from django.urls import path, include
import article.views

urlpatterns = [
    path('articles/', article.views.articles),
    path('articles/<int:article_id>/', article.views.article),
]
