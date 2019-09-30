from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect, render
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from article.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    # TODO: change cur_page
    current_page = Paginator(all_articles, 2)
    response = render_to_response("articles.html", {
        "articles": current_page.page(page_number),
        "username": auth.get_user(request).username})
    response.set_cookie("page_number", page_number)
    return response


@csrf_protect
def article(request, article_id=1):
    comment_form = CommentForm
    args = {"article": Article.objects.get(id=article_id),
            "comments": Comments.objects.filter(article_reference_id=article_id),
            "form": comment_form,
            "username": auth.get_user(request).username}
    return render(request, "article.html", args)


def add_like(request, article_id=1):
    page_number = request.COOKIES.get("page_number", 1)
    response = redirect(f"/page/{page_number}")
    try:
        if str(article_id) not in request.COOKIES:
            article = Article.objects.get(id=article_id)
            article.likes += 1
            article.save()
            response.set_cookie(str(article_id), "add_like test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return response


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