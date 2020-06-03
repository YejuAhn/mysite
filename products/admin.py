from django.contrib import admin
from import_export import resources
from .models import Product
from import_export.admin import ImportExportModelAdmin

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product



class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource



admin.site.register(Product,ProductAdmin)
