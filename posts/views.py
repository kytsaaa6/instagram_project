from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from accounts.models import Account, Follow
from comments.models import Comment
from .models import Post
from .forms import PostForm


def post(request):
    try:
        follow = Account.objects.get(username=request.user)
        if follow.follower.all().exists():
            follow_list = follow.follower.values_list('follow_id', flat=True)
            follower_list = follow.follower.values('follower_id')
            follow_post_list = follow_list.union(follower_list, all=False)
            data = Post.objects.filter(account_id__in=follow_post_list)
        else:
            data = Post.objects.all()
        context = {
            'data': data,
        }
    except:
        data = Post.objects.all()
        context = {
            'data': data,
        }
    return render(request, 'posts/base.html', context)

def explore(request):
    post = Post.objects.order_by("?")

    context = {
        'post':post
    }

    return render(request, 'posts/explore.html', context)

def mypage(request, account):
    member = Account.objects.get(username=account)
    try:
        data = Follow.objects.get(follow=member, follower=request.user)
        context = {
            'data': member.post_set.all,
            'member': member,
            'account': data
        }
    except:
        context = {
            'data': member.post_set.all,
            'member': member,
        }
    return render(request, 'posts/page.html', context)

"""
    member = get_object_or_404(Account, username=account)
    if Follow.objects.filter(follow=member, follower=request.user).exists():
        follow = Follow.objects.get(follow=member, follower=request.user)
        context = {
            'data':member.post_set.all,
            'member':member,
            'follow':follow,
        }
    else:
        context = {
            'data':member.post_set.all,
            'member':member,
            'follow':follow,
    }
    return render(request, 'posts/page.html', context)
"""
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