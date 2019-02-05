from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.core.urlresolvers import reverse
from .forms import AccountCreationForm, AccountLoginForm
from django.contrib.auth import views as auth_views
from .models import Account


def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        userform = AccountCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return redirect("signup_ok")

    elif request.method == "GET":
        userform = AccountCreationForm()

    return render(request, "registration/signup.html", {"userform":userform,})


class Login(auth_views.LoginView):
    """
    Display the login form and handle the login action.
    """
    form_class = AccountLoginForm