from rest_framework import serializers
from Blog.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'url',
            'description',
            'author',
            'text',
            'pub_date',
            'image',
        ]