from django.shortcuts import render, get_object_or_404
from .models import Article
from rest_framework import viewsets  # add this


# def article_detail_view(request):
#     obj = Article.objects.get(id=1)
#     context = {
#         'object': obj
#     }
#     return render(request, "Blog/article_detail.html", context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Article, id = id)
    context = {
        "object" : obj
    }
    return render(request, "Blog/article_detail.html", context)

def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "Blog/article_list.html", context)
