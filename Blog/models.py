from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField(default= "https://www.google.com/")
    description = models.TextField(blank = True, null = True)
    author = models.CharField(max_length = 30)
    text = models.TextField(blank = True, null = True)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'gallery', default='gallery/FitSimplify.jpg')

    def get_absolute_url(self):
        return reverse("Blog:article-detail", kwargs={"id": self.id})


