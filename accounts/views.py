from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
#from django.core.urlresolvers import reverse
from .forms import AccountCreationForm, AccountLoginForm
from django.contrib.auth import views as auth_views
from .models import Account, Follow


def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        userform = AccountCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return redirect("login")

    elif request.method == "GET":
        userform = AccountCreationForm()

    return render(request, "registration/signup.html", {"userform":userform,})


class Login(auth_views.LoginView):
    """
    Display the login form and handle the login action.
    """
    form_class = AccountLoginForm


def follow(request, account):
    account = get_object_or_404(Account, username=account)
    if Follow.objects.filter(follow=account, follower=request.user).exists():
        data = Follow.objects.get(follow=account, follower=request.user)
        data.delete()

    else:
        Follow.objects.create(
            follow=account,
            follower=request.user
        )
        """
    try:
        account = get_object_or_404(Account, username=account)
        data = Follow.objects.get(follow=account, follower=request.user)
        data.delete()
    except:
        account = get_object_or_404(Account, username=account)
        Follow.objects.create(
            follow=account,
            follower=request.user
        )"""

    return redirect("mypage", account=account)
