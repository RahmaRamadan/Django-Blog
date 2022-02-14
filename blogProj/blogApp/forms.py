from dataclasses import fields
from re import L
from django import forms
from .models import Post ,Comment
#auth import
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # fields = ('__all__')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        # fields = ('title','content','category','user','tags','postpicture')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        