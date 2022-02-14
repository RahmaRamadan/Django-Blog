from dataclasses import fields
from re import L
from django import forms
# auth import
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
