from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.core.urlresolvers import reverse
from accounts.forms import AccountCreationForm, AccountLoginForm
from django.contrib.auth import views as auth_views


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

