from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect, render
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth


def articles(request):
    return render_to_response("articles.html", {
        "articles": Article.objects.all(),
        "username": auth.get_user(request).username})


@csrf_protect
def article(request, article_id=1):
    comment_form = CommentForm
    args = {"article": Article.objects.get(id=article_id),
            "comments": Comments.objects.filter(article_reference_id=article_id),
            "form": comment_form,
            "username": auth.get_user(request).username}
    return render(request, "article.html", args)


def add_like(request, article_id=1):
    try:
        if str(article_id) not in request.COOKIES:
            article = Article.objects.get(id=article_id)
            article.likes += 1
            article.save()
            response = redirect("/")
            response.set_cookie(str(article_id), "add_like test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect("/")


def add_comment(request, article_id=1):
    if request.POST and request.session.get("pause", True):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_reference = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session["pause"] = False
    return redirect(f"/articles/{article_id}/")