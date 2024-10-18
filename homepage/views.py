from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post

class News_view(ListView):
    model = Post
    template_name = 'home.html'

class Post_detail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'