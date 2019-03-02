from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs),
        del self.fields['password2']


class AccountLoginForm(AuthenticationForm):
    username = UsernameField(
        label=("사용자이름 "),
        widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=("비밀번호 "),
        strip=False,
        widget=forms.PasswordInput,
    )

