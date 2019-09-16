from django.shortcuts import render, reverse, redirect 
from .models import Blog, Post, Connection
from django.contrib.auth import get_user_model
from blog.forms import BlogCreateAndEditForm, PostCreateAndEditForm
from django.db.models import Q


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def blog(request, id):
    blog = Blog.objects.get(id=id)
    post = Post.objects.filter(blog=blog)
    context = {
        'blog': blog,
        'post': post,
    }

    return render(request, 'blog.html', context)


def myblog(request):
    blog = Blog.objects.get(user=request.user)
    post = Post.objects.filter(blog=blog)
    context = {
        'blog': blog,
        'post': post,
    }

    return render(request, 'blog.html', context)


def post(request, id):
    post = Post.objects.get(id=id)
    blog = Blog.objects.get(post=post)
    context = {
        'post': post,
        'blog': blog,
    }

    return render(request, 'post.html', context)


def create_blog(request):
    blog = None
    form_class = BlogCreateAndEditForm
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('myblog')
    else:
        form = form_class(instance=blog)

    return render(request, 'create_blog.html', {
        'form': form,
        'blog': blog,
    })


def edit_blog(request, id):
    blog = Blog.objects.get(id=id)
    form_class = BlogCreateAndEditForm
    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog', id=blog.id)
    else:
        form = form_class(instance=blog)

    return render(request, 'edit_blog.html', {
        'form': form,
        'blog': blog,
    })


def create_post(request):
    print('hi')
    form_class = PostCreateAndEditForm
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            my_blog = Blog.objects.get(user=request.user)
            post.blog = my_blog
            post.save()
            return redirect('myblog')
    else:
        form = form_class()

    return render(request, 'create_post.html', {
        'form': form,
    })


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('myblog')


def edit_post(request, id):
    post = Post.objects.get(id=id)
    form_class = PostCreateAndEditForm
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('myblog')
    else:
        form = form_class(instance=post)

    return render(request, 'edit_post.html', {
        'form': form,
        'post': post,
    })


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(postTitle__icontains=query) | Q(postText__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'submitbutton': submitbutton
            }
            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    return render(request, 'search.html')


def follow(request, id):
    following = request.user
    beingfollowed = get_user_model().objects.get(id=id)
    Connection.objects.create(following=following, beingFollowed=beingfollowed)
    return redirect('following')


def following(request):
    beingfollowed = Connection.objects.filter(following=request.user)
    context = {
        'beingfollowed': beingfollowed,
    }
    return render(request, 'beingFollowed.html', context)
