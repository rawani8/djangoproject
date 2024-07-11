from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, Category

def main(request):
    return render(request, 'main.html')

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def blogs(request):
    blogs = Post.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def blogdetails(request, id):
    blog = get_object_or_404(Post, id=id)
    return render(request, 'blogdetails.html', {'blog': blog})