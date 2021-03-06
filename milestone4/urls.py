"""milestone4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from threeauth.views import logout, login, registration, user_profile
from threeauth import urls as url_auth
from threeshop import urls as url_products
from threeshop.views import all_products
from threecart import urls as urls_cart
from threesearch import urls as urls_search
from threecheckout import urls as urls_checkout
from threecontact import urls as urls_contact
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    
    path('admin/', admin.site.urls),
    #3lite URLSs
    path('', include('threelite.urls')),
    #User Auth URLS
    path('auth/', include(url_auth)),
    #blogurls
    path('blog/', include('posts.urls')),
    #shop urls
    path('shop/', all_products, name="shop"),
    path('products/', include(url_products)),
    path('cart/', include(urls_cart)),
    path('search/', include(urls_search)),
    path('checkout/', include(urls_checkout)),
    #media urls
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    #contact urls
    path('contact/', include(urls_contact))

] 
