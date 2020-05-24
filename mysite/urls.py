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
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from mysite import settings
from pages.views import home_view, contact_view, about_view, social_view
from products.views import product_detail_view, product_create_view
from accounts.views import register_page
from accounts.views import login_page
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html')),
    path('contact/', contact_view),
    path('about/', about_view),
    path('social/', social_view),
    path('admin/', admin.site.urls),
    path('create/', product_create_view),
    path('product/', product_detail_view) ,
    path('products/', include('products.urls')),
    path('Blog/', include('Blog.urls')),
    path('polls/', include('polls.urls')),
    path('register/', register_page),
    path('login/', login_page, name = 'auth_login'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/products/', include("products.api.urls")),
    url(r'^api/articles/', include("Blog.api.urls")),
    url(r'^api/polls/', include("polls.api.urls")),
    url(r'^graphql$', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     # your integrate path
#     re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
# ]
