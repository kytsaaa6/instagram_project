from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from posts.models import Post, Tag
from accounts.models import Account, Follow
from posts.forms import PostForm
from accounts.forms import AccountCreationForm


def post(request):
    userform = AccountCreationForm()
    if userform.is_valid():
        userform.save()
    try:
        follow = Account.objects.get(username=request.user)
        if follow.followers.all().exists():
            follow_list = follow.followers.values_list('follow_id', flat=True)
            follower_list = follow.followers.values('follower_id')
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
            'userform': userform,
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


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.account = request.user
            posts.save()
            posts.tag_save()
            return redirect('post_mypage', account=request.user)
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
            return redirect('post_mypage', account=request.user)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_update.html', {'form': form})


def delete(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
        data = Post.objects.all()
    except:
        data = Post.objects.all()

    context = {
        'data': data,
    }
    return render(request, 'posts/post.html', context)


def post_like(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    if post.post_like.filter(id=user.id).exists():
        post.post_like.remove(user)
    else:
        post.post_like.add(user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def explore(request):
    post = Post.objects.order_by("?")

    context = {
        'data': post,
    }
    return render(request, 'posts/post_explore.html', context)


def tag_list(request, tag):
    tag_list = Tag.objects.get(name=tag)
    posts = tag_list.post_set.all()
    context = {
        'data': posts,
        'tag': tag_list
    }

    return render(request, 'posts/post_tag_list.html', context)


def search(request):
    post_search = Post.objects.all()
    search = request.GET.get('search', '')
    searchs = post_search.filter(account__username__contains=search)|post_search.filter(text__contains='#'+search)

    context= {
           'data': searchs,
           'search': search,
    }
    return render(request, 'posts/search.html', context)

