from django.contrib import admin
from article.models import Article, Comments


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'date']
    inlines = [ArticleInline]
    list_filter = ['date']


admin.site.register(Article, ArticleAdmin)