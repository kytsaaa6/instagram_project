from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import AccountCreationForm, AccountLoginForm
from django.contrib.auth import views as auth_views
from accounts.models import Account, Follow


def signup(request):
    if request.method == "POST":
        userform = AccountCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return redirect("/accounts/login")

    elif request.method == "GET":
        userform = AccountCreationForm()

    return render(request, "registration/signup.html", {"userform":userform})

class Login(auth_views.LoginView):
    form_class = AccountLoginForm


def follow(request, account):
    try:
        account = get_object_or_404(Account, username=account)
        data = Follow.objects.get(follow=account, follower=request.user)
        data.delete()
    except:
        account = get_object_or_404(Account, username=account)  # 유저 모델에서 팔로우를 한 유저의 정보를 가져옴
        Follow.objects.create(
            follow=account,
            follower=request.user
        )
        #    data = Follow()
        #    data.follow = account
        #    data.follower = request.user
        #    data.save()
    return redirect('post_mypage', account=account)



