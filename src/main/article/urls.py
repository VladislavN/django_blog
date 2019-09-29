import re
from django.contrib import admin
from django.urls import path, include
import article.views

urlpatterns = [
    path('', article.views.articles),
    path('articles/', article.views.articles),
    path('articles/<int:article_id>/', article.views.article),
    path('articles/addlike/<int:article_id>/', article.views.add_like),
    path('articles/addcomment/<int:article_id>/', article.views.add_comment),
]
