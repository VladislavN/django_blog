from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response


def basic_one(request):
    view = "basic_one"
    html = f"<html> " \
           f"<body>" \
           f"This is {view} view" \
           f"</body>" \
           f"</html>"
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    t = get_template("view.html")
    html = t.render({"name": view})
    return HttpResponse(html)


def template_three_simple(request):
    view = "template_three_simple"
    return render_to_response("view.html", {"name": view})