from django import forms
from django.contrib.auth.forms import UserCreationForm   # 사용자 이름, 비밀 번호, 비밀 번호 확인
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")