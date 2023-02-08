from django.shortcuts import render
from .models import Blog

def home(request):
    posts = Blog.objects.all()
    return render(request, "my_blog/home.html", { 'posts': posts })

def about(request):
    return render(request, "my_blog/about.html")

