from django.shortcuts import render
from posts.models import Post
from django.utils import timezone

# Create your views here.

def index(request):
	return render(request, 'threelite/index.html')

def portfolio(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'threelite/portfolio.html', {'posts':posts})