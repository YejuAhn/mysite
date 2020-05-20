from django.urls import re_path

from .views import QuestionListAPIView, QuestionRetrieveAPIView

app_name = 'articles-api'

urlpatterns = [
    re_path(r'^$', QuestionListAPIView.as_view(), name='list'),
    #product-detail view
    re_path(r'^(?P<id>\d+)/$', QuestionRetrieveAPIView.as_view(), name='detail')
]
