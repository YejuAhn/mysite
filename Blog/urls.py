
from django.urls import path

app_name = 'Blog'

from .views import(
    article_detail_view,
)

urlpatterns = [
    path('', article_detail_view, name = 'article-detail')
]


