from django.contrib.auth.models import User
from django import forms
from django_countries.data import COUNTRIES
from django.contrib.auth.forms import UserCreationForm
from django_countries.widgets import CountrySelectWidget
from .models import Post


# from blog.choices import *


class CountryForm(forms.Form):
    country = forms.ChoiceField(sorted(COUNTRIES.items()))


class CreateUserForm(UserCreationForm):  # 내장 회원가입 폼을 상속받아서 확장한다.
    email = forms.EmailField(required=True)  # 이메일 필드 추가

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):  # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False)  # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):

    photo = forms.ImageField(label='', required=False)

    class Meta:
        model = Post
        fields = ('country', 'postcategory','classification','title', 'name', 'address', 'contents','hashtag','photo', 'video')
        widgets = {'country': CountrySelectWidget()}

class ActivityPostForm(forms.ModelForm):

    photo = forms.ImageField(label='', required=False)

    class Meta:
        model = Post
        fields = ('postcategory', 'title', 'hashtag', 'photo', 'video')