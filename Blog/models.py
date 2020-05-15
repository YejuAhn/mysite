from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField(default= "https://www.google.com/")
    description = models.TextField(blank = True, null = True)
    author = models.CharField(max_length = 30)
    text = models.TextField(blank = True, null = True)
    pub_date = models.DateTimeField('date published')


    # def get_absolute_url(self):
        # return reverse("products:product-detail", kwargs={"id": self.id})