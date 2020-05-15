from django.shortcuts import render
from .models import Article


def article_detail_view(request):
    obj = Article.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "Blog/article_detail.html", context)

