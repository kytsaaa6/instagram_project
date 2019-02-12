from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from accounts.models import Account, Follow
from posts.forms import PostForm


def post(request):
    follow = Account.objects.get(username=request.user)
    if follow.followers.all().exists():
        follow_list = follow.followers.values_list('follow_id', flat=True)
        follower_list = follow.followers.values('follower_id')
        follow_post_list = follow_list.union(follower_list, all=False)
        data = Post.objects.filter(account_id__in=follow_post_list)
    else:
        data = Post.objects.all()

    likes = list()

    for posts in data:
        if posts.like_set.filter(account=request.user).exists():
            likes.append(True)
        else:
            likes.append(False)

    context = {
        'data': data,
        'likes': likes
    }
    return render(request, 'posts/post.html', context)


def my_page(request, account):
    member = Account.objects.get(username=account)
    try:
        follow = Follow.objects.get(follow=member, follower=request.user)
        context = {
            'data': member.post_set.all,
            'member': member,
            'follow': follow
        }
    except:
        context = {
            'data': member.post_set.all,
            'member': member,
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

    likes = list()

    for posts in data:
        if posts.like_set.filter(account=request.user).exists():
            likes.append(True)
        else:
            likes.append(False)

    context = {
        'data': data,
        'likes': likes
    }
    return render(request, 'posts/post.html', context)


def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # 중간자 모델 Like 를 사용하여, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다.
    post_like, post_like_created = post.like_set.get_or_create(account=request.user)

    if not post_like_created:
        post_like.delete()

    return redirect('post')

