# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Article(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default=timezone.now)
    article_reference = models.ForeignKey(Article, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
