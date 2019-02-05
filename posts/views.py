from django.shortcuts import render, redirect
from posts.models import Post
from accounts.models import Account
from posts.forms import PostForm

def post(request):
    data = Post.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'posts/post.html', context)


def mypage(request, account):
    member = Account.objects.get(username=account)
    data = Post.objects.filter(account=member)
    context = {
        'data': data
    }
    return render(request, 'posts/post_mypage.html', context)


def create(request):
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


def update(request, account, post_id):
    pass


def delete(request):
    pass



