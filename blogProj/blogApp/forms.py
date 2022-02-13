from dataclasses import fields
from re import L
from django import forms
from .models import Post
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
        fields = ('title','content','category','user','tags')
        # fields = ('__all__')