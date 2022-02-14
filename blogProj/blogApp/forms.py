from dataclasses import fields
from re import L
from django import forms

from .models import Post ,Comment

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')


class UsersForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ["name", "followers"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'follower': forms.Select(attrs={'class': 'form-control'}),

        }
        # fields = ('__all__')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('__all__')
        fields = ('title','content','category','user','tags','postpicture')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        


