from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from accounts.models import Account
from posts.forms import PostForm
from comments.models import Comment


def post(request):
    data = Post.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'posts/post.html', context)


def my_page(request, account):
    member = Account.objects.get(username=account)
    context = {
        'data': member.post_set.all,
    }
    return render(request, 'posts/post_mypage.html', context)


def create(request, account):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)  # 중복 DB save를 방지
            posts.account = request.user
            posts.save()
            return redirect('post')
    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {'form': form})


def update(request, post_id):
    post = Post.objects.get(pk=post_id)
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


def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    data = Post.objects.all()
    context = {
        'data':data
    }
    return render(request,'posts/post.html',context)



