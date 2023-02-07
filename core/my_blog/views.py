from django.shortcuts import render

def home(request):
    return render(request, "my_blog/home.html")

def about(request):
    return render(request, "my_blog/about.html")

