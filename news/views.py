from django.shortcuts import render
from .models import Post, Topico

# Create your views here.

def home(request):
   posts = Post.objects.order_by('-data_publicacao')[:6]
   context = {
      'posts': posts
   }
   return render(request, 'news/home.html', context)

def post_detail(request, post_id):
   posts = Post.objects.get(pk=post_id)
   context = {
      'posts' : posts
   }
   return render(request, 'news/post_detail.html', context)