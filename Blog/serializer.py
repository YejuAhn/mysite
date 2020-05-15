from rest_framework import serializers
from .models import Article


class BlogSerializer(serializers.ModelSerizlier):
    class Meta:
        model = Article
        fields = ('pk', 'title', 'url', 'description', 'author', 'text', 'pub_date')

        def __str__(self):
            return self.title





