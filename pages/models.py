from django.db import models
from django.urls import reverse


class Menu(models.Model):
    STATUS_CHOICES = (
        ('articles', 'Articles'),
        ('polls', 'Polls'),
        ('products', 'Products'),
    )

    menu_title = models.CharField(max_length = 200)
    slug = models.SlugField()
    show_in_menu = models.BooleanField(default= False)
    status = models.CharField(max_length= 10, choices = STATUS_CHOICES, default = 'draft')

    # base_urls = models.CharField(max_length=100, blank = True, null = True)
    # description = models.TextField(blank = True, null = True)

    def get_absolute_url(self):
        return reverse('page_detail', args=[self.slug])

    # class Admin:
    #     pass
    #
    # def __unicode__(self):
    #     return "%s" %self.name
    #
    # def save(self):
    #     current = 10
    #     for item in MenuItem.objects.filter(menu = self).order_by('order'):
    #         item.order = current
    #         item.save()
    #         current += 10

#
#
# class MenuItem(models.Model):
#     menu = models.ForeignKey(Menu)
#     order = models.IntegerField()
#     link_url = models.CharField(max_length = 100, help_text = 'URL or URI to the content, eg / about or http://foo.com/')
#     title = models.CharField(max_lenght = 100)
#     login_required = models.BooleanField(blank = True, null = True)
#
#     class Admin:
#         pass
#
#     def __unicode__(self):
#         return "%s %s. %s" %(self.menu.slug, self.order, self.title)


