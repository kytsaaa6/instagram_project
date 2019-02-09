from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Account
from comments.models import Comment
from .models import Post
from .forms import PostForm


def post(request):
    data = Post.objects.all()
#    comment = Comment.objects.all()
    context = {
        'data':data,
#        'comment':comment,
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

def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.account = request.user
            post.save()
            return redirect('post')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_update.html', {'form': form})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
        #if request.POST['password'] == article.password:
    post.delete()

    return redirect('post')  # 첫페이지로 이동하기


def post_like(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    if post.post_like.filter(id=user.id).exists():
        post.post_like.remove(user)
    else:
        post.post_like.add(user)

    return redirect('post')

# Create your views here.