from dataclasses import fields
from re import L
from django import forms
from .models import Post, Comment, CommentReply, ForbiddenWord
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class UsersForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ["name", "followers"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'follower': forms.Select(attrs={'class': 'form-control'}),
        }


class CategoryFormAdmin(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ["name"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags', 'postpicture')
        widgets = {
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }


class ForbiddenWordForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWord
        fields = ('name',)
