from django.shortcuts import render, redirect, get_object_or_404
from blog. models import BlogPost
from blog. forms import CreateBlogPostForm
from account.models import User
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

def CreateBlogView(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = User.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
    
    return render(request, 'blog/create_blog.html', {'form':form})

def BlogDetailView(request):
    blog_post = get_object_or_404(BlogPost)
    return render(request, 'blog/detail_view.html', {'blog_post':blog_post})
