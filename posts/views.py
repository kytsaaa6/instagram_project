from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Account
from .models import Post
from .forms import PostForm

def post(request):
    data = Post.objects.all()
    context = {
        'data':data,
    }
    return render(request, 'posts/base.html', context)

def mypage(request, username):
    if request.method == 'GET':
        data = Post.objects.all()
        data = data.filter(account=request.user)
        context = {
            'data':data,
        }
    return render(request, 'posts/page.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid():
            post = form.save(commit=False)  # 중복 DB save를 방지
            post.account = request.user
            post.save()
            return redirect('post')
    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {
        'form': form,
    })

def update(request):
    pass

def delete(request):
    pass

# Create your views here.