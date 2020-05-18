"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path

from mysite import settings
# from pages.views import home_view, contact_view, about_view, social_view
from pages.views import FrontendRenderView
from products.views import product_detail_view, product_create_view
from django.conf.urls.static import static

urlpatterns = [
    # path('', home_view, name = 'home'),
    # path('contact/', contact_view),
    # path('about/', about_view),
    # path('social/', social_view),
    # path('admin/', admin.site.urls),
    # path('create/', product_create_view),
    # path('product/', product_detail_view) ,
    # path('products/', include('products.urls')),
    # path('Blog/', include('Blog.urls')),
    # path('polls/', include('polls.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/products/', include("products.api.urls")),
    re_path(r'^api/articles/', include("Blog.api.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    # your integrate path
    re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
]
