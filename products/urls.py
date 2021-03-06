from django.contrib import admin
from django.urls import path

# from pages.views import home_view, contact_view, about_view

app_name = 'products'
from .views import(
    product_detail_view,
    product_create_view,
    render_initial_data,
    dynamic_lookup_view,
    product_list_view
)

urlpatterns = [
    path('<int:id>/', dynamic_lookup_view, name = 'product-detail'),
    path('', product_list_view, name = 'product-list'),
    path('create_product', product_create_view, name = 'product-create')
]

