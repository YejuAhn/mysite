from django.urls import re_path

from .views import ArticleListAPIView, ArticleRetrieveAPIView

app_name = 'articles-api'

urlpatterns = [
    re_path(r'^$', ArticleListAPIView.as_view(), name='list'),
    #product-detail view
    re_path(r'^(?P<id>\d+)/$', ArticleRetrieveAPIView.as_view(), name='detail')
]
