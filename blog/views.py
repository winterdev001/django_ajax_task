from django.shortcuts import render, redirect
from blog.models import Blog
from blog.forms import BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 
from django.http import HttpResponse

# Create your views here.
@login_required
def index(request):  
    blogs = Blog.objects.all() 
    liked = []     
    for blog in blogs:
        if(blog.likes.filter(id=request.user.id).exists()):
            liked.append(blog.id)
    params = {
        'blogs': blogs,
        'liked':liked,
    }
    return render(request, 'blogs/index.html', params)

@login_required
def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        user = request.user
        blog = Blog(title=title, description= description, writer = user)
        blog.save()
        messages.success(request,"Blog created successfully")
        return redirect('index')
    else:
        params = {
            'form': BlogForm(),
        }
        return render(request, 'blogs/create.html',params)

@login_required
def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    params = {
        'blog': blog,
    }
    return render(request, 'blogs/detail.html', params)

@login_required
def edit(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    if(request.method == 'POST'):
        blog.title = request.POST['title']
        blog.description = request.POST['description']
        blog.save()
        return redirect('detail', blog_id)
    else:
        form = BlogForm(initial={
            'title':blog.title,
            'description' : blog.description,
        })
        params = {
            'blog': blog,
            'form': form
            }
        return render(request, 'blogs/edit.html', params)

@login_required
def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if(request.method == 'POST'):
        blog.delete()
        return redirect('index')
    else:
        params = {
            'blog': blog,
        }
        return render(request, 'blogs/delete.html', params)
    
@login_required
def blogLike(request, blog_id):
    blogs = Blog.objects.all() 
    liked = [] 

    for liked_blog in blogs:
        if(liked_blog.likes.filter(id=request.user.id).exists()):
            liked.append(liked_blog.id)
            
    blog = Blog.objects.get(id=blog_id) 
    if blog.likes.filter(id = request.user.id).exists():
        liked.remove(blog.id)
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)
        liked.append(blog.id)
        
    params = {
        'blogs':blogs,
        'liked' : liked,
    }
    return render(request,'blogs/index.html',params)
 

    
    