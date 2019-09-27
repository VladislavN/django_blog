from django.db import models


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

    text = models.TextField()
    article_reference = models.ForeignKey(Article, on_delete=models.CASCADE)
