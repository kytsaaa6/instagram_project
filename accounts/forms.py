from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django import forms
from accounts.models import Account
from django.contrib.auth import authenticate


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("phone", "email", "fullname", "username")
        field_classes = {'username': UsernameField}

    phone = forms.CharField(
        label=("핸드폰번호"),
        strip=False,
        widget=forms.NumberInput,
    )

    email = forms.CharField(
        label=("이메일"),
        strip=False,
       widget=forms.EmailInput,
    )

    fullname = forms.CharField(
        label=("성명"),
        strip=False,
        widget=forms.TextInput,
    )

    username = forms.CharField(
        label=("사용자 이름"),
        strip=False,
        widget=forms.TextInput,
    )

    password1 = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label=("비밀번호 확인"),
        widget=forms.PasswordInput,
        strip=False,
    )


class AccountLoginForm(AuthenticationForm):

    phone = forms.CharField(
        label=("핸드폰번호"),
        strip=False,
        widget=forms.NumberInput,
    )

    email = forms.CharField(
        label=("이메일"),
        strip=False,
        widget=forms.EmailInput,
    )
"""
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        
        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password, phone=phone, email=email)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
"""