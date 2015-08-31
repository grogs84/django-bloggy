from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader

from blog.models import Post

### helper functions ####
def encode_url(url):
	return url.replace(' ', '_')

def get_popular_posts():
	posts = Post.objects.order_by('-views')[:5]
	for post in posts:
		post.url = encode_url(post.title)
	return posts

### views ####
def index(request):
	latest_posts  = Post.objects.all().order_by('-created_at')
	t = loader.get_template('blog/index.html')
	context_dict = {
		'latest_posts': latest_posts,
		'popular_posts': get_popular_posts(),
		}
	for post in latest_posts:
		post.url = encode_url(post.title)
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def post(request, post_url):
	single_post = get_object_or_404(Post, title=post_url.replace('_', ' '))
	single_post.views += 1
	single_post.save()
	context_dict = {
		'single_post': single_post,
		'popular_posts': get_popular_posts(),
	}
	t = loader.get_template('blog/post.html')
	c = Context(context_dict)
	return HttpResponse(t.render(c))