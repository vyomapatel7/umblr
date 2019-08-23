from django.shortcuts import render
from .models import Blog


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def myblog(request):
    blog = Blog.objects.get(user=request.user)
    context = {
        'blog': blog,
    }

    return render(request, 'blog.html', context)
