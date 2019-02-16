from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from accounts.models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("phone", "email", "name", "username")
        field_classes = {'username': UsernameField}

    phone = forms.CharField(
        label=("휴대폰 번호"),
        strip=False,
        widget=forms.NumberInput,
    )

    email = forms.CharField(
        label=("이메일 주소"),
        strip=False,
        widget=forms.EmailInput,
    )

    name = forms.CharField(
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
        label=("비밀번호 재입력"),
        strip=False,
        widget=forms.PasswordInput,
    )

"""class AccountLoginForm(AuthenticationForm):
    phone = forms.CharField(
        label=("휴대폰 번호"),
        strip=False,
        widget=forms.NumberInput,
    )
    email = forms.CharField(
        label=("이메일 주소"),
        strip=False,
        widget=forms.EmailInput,
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('eamil')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, phone=phone, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
        """
