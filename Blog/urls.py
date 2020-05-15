
from django.urls import path

app_name = 'Blog'

from .views import (
    dynamic_lookup_view,
    article_list_view
)

urlpatterns = [
    path('<int:id>/', dynamic_lookup_view, name='article-detail'),
    path('', article_list_view, name = 'article-list'),
]


