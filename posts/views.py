from django.http import HttpResponseRedirect, Http404
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
            posts = Post.objects.filter(account_id__in=follow_post_list)
        else:
            posts = Post.objects.all()

        context = {
            'posts': posts,
        }
    except Account.DoesNotExist:
        posts = Post.objects.all()
        context = {
            'posts': posts,
            'userform': userform,
        }
    return render(request, 'posts/post.html', context)


def my_page(request, account):
    try:
        member = Account.objects.get(username=account)
    except Account.DoesNotExist:
        raise Http404

    try:
        follow = Follow.objects.get(follow=member, follower=request.user)
        context = {
            'members': member.post_set.all,
            'member': member,
            'follow': follow
        }
    except Follow.DoesNotExist:
        context = {
            'members': member.post_set.all,
            'member': member,
        }
    return render(request, 'posts/post_mypage.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
<<<<<<< HEAD
            create_post = form.save(commit=False)
            create_post.account = request.user
            create_post.save()
            create_post.tag_save()
=======
            post_create = form.save(commit=False)
            post_create.account = request.user
            post_create.save()
            post_create.tag_save()
>>>>>>> origin/insta_ho
            return redirect('post_mypage', account=request.user)
    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {'form': form})


def update(request, post_id):
    try:
        update_post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = PostForm(request.POST, instance=update_post)
        if form.is_valid():
<<<<<<< HEAD
            update_post = form.save(commit=False)
            update_post.account = request.user
            update_post.save()
            update_post.tag_save()
=======
            post_update = form.save(commit=False)
            post_update.account = request.user
            post_update.save()
            post_update.tag_save()
>>>>>>> origin/insta_ho
            return redirect('post_mypage', account=request.user)
    else:
        form = PostForm(instance=update_post)

    return render(request, 'posts/post_update.html', {'form': form})


def delete(request, post_id):
    try:
        post_remove = Post.objects.get(pk=post_id)
        post_remove.delete()
    except Post.DoesNotExist:
        raise Http404

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def post_like(request, post_id):
    user = request.user
    try:
        like = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    if like.post_like.filter(id=user.id).exists():
        like.post_like.remove(user)
    else:
        like.post_like.add(user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def explore(request):
    post_explore = Post.objects.exclude(photo__isnull=True).exclude(photo__exact='').order_by("?")
    # 이미지가 없거나 빈문자열이 아닌것을 랜덤으로 쿼리셋

    context = {
        'post_explore': post_explore,
    }
    return render(request, 'posts/post_explore.html', context)


def tag_list(request, tag):
    try:
        hash_tag = Tag.objects.get(name=tag)
    except Tag.DoesNotExist:
        raise Http404
    
    hash_post = hash_tag.post_set.all()
    context = {
        'posts': hash_post,
        'tag': hash_tag
    }

    return render(request, 'posts/post_tag_list.html', context)


def search(request):
    post_search = Post.objects.all()
    search_context = request.GET.get('search')
    try:
        if search_context:
            search_result = post_search.filter(account__username__contains=search_context) \
                            | post_search.filter(text__contains='#'+search_context)

        context = {
            'search_result': search_result,
            'search': search_context,
        }

        return render(request, 'posts/search.html', context)

    except UnboundLocalError:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




