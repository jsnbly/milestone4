from django.urls import path
from . import views
from posts.views import get_posts

urlpatterns = [
	path('', views.index, name='index'),
	path('portfolio/', views.portfolio, name='portfolio')
]