from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from accounts.models import Account, Follow
from accounts.forms import AccountCreationForm
from .models import Post, Tag
from .forms import PostForm


def post(request):
    userform = AccountCreationForm()
    if userform.is_valid():
        userform.save()
    try:
        follow = Account.objects.get(username=request.user)
        if follow.follower.all().exists():
            follow_list = follow.follower.values_list('follow_id', flat=True)
            follower_list = follow.follower.values('follower_id')
            follow_post_list = follow_list.union(follower_list, all=False)
            post_list = Post.objects.filter(account_id__in=follow_post_list)
        else:
            post_list = Post.objects.all()
        context = {
            'post_list': post_list,
        }
    except Account.DoesNotExist:
        post_list = Post.objects.all()
        context = {
            'post_list': post_list,
            'userform': userform,
        }
    return render(request, 'posts/base.html', context)


def explore(request):
    explore_post = Post.objects.order_by("?")

    context = {
        'explore_post': explore_post
    }

    return render(request, 'posts/explore.html', context)


def mypage(request, account):
    member = Account.objects.get(username=account)
    try:
        post_mypage = Follow.objects.get(follow=member, follower=request.user)
        context = {
            'post_mypage': member.post_set.all,
            'member': member,
            'account': post_mypage
        }
    except Follow.DoesNotExist:
        context = {
            'post_mypage': member.post_set.all,
            'member': member,
        }
    return render(request, 'posts/page.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid():
            post_create = form.save(commit=False)  # 중복 DB save를 방지
            post_create.account = request.user
            post_create.save()
            post_create.tag_save()
            return redirect('mypage', account=request.user)
    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {
        'form': form,
    })


def update(request, pk):
    post_update = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post_update)
        if form.is_valid():
            post_update = form.save(commit=False)
            post_update.account = request.user
            post_update.save()
            post_update.tag_save()
            return redirect('mypage', account=request.user)
    else:
        form = PostForm(instance=post_update)
    return render(request, 'posts/post_update.html', {'form': form})


def delete(request, pk):
    if request.method == "GET":
        post_delete = Post.objects.get(pk=pk)
        post_delete.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def post_like(request, pk):
    user = request.user
    like = Post.objects.get(pk=pk)
    if like.post_like.filter(id=user.id).exists():
        like.post_like.remove(user)
    else:
        like.post_like.add(user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def tag_list(request, tag):
    tag = Tag.objects.get(name=tag)
    tag_post = tag.post_set.all()

    context = {
        'tag': tag,
        'tag_post': tag_post,
    }

    return render(request, 'posts/post_tag_list.html', context)


def search(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')  # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q:  # q가 있으면
        search_post = qs.filter(account__username__contains=q) | qs.filter(text__contains='#'+q)  # 제목에 q가 포함되어 있는 레코드만 필터링

        context = {
            'search_post': search_post,
        }
        return render(request, 'posts/search.html', context)

    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
