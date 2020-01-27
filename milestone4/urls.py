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
from threeauth.views import logout, login, register, user_profile
from threeshop import urls as url_products
from threeshop.views import all_products
from threecart import urls as urls_cart
from threesearch import urls as urls_search
from threecheckout import urls as urls_checkout
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    
    path('admin/', admin.site.urls),
    #3lite URLSs
    path('', include('threelite.urls')),
    #User Auth URLS
    path('auth/', include('threeauth.urls')),
    path('auth/logout/', logout, name="logout"),
    path('auth/login/', login, name="login"),
    path('auth/register', register, name="registration"),
    path('auth/profile', user_profile, name="profile"),
    #passwordreset needs to be completed
    #path('auth/password-reset', include(url_reset)),
    #blogurls
    path('blog/', include('threeblog.urls')),
    #shop urls
    path('shop/', all_products, name="shop"),
    path('products/', include(url_products)),
    path('cart/', include(urls_cart)),
    path('search/', include(urls_search)),
    path('checkout/', include(urls_checkout)),
    path('media/(?P<path>.*)', static.serve, {'document_root':MEDIA_ROOT}),
]
