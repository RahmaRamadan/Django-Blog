from tkinter import CASCADE
from django import forms
from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
# Create your models here.


# class User(models.Model):
#     class Meta:
#         ordering = ['pk']
#     username = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username


class Category(models.Model):
    class Meta:
        ordering = ['pk']
    name = models.CharField(max_length=50)
    followers = models.ManyToManyField(User)
    def __str__(self):
        return self.name 
    
    def __str__(self):
        return self.name

    def show_followers(self):
        return "\n".join([a.username for a in self.followers.all()])
    
class UsersCategories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Tag(models.Model):
    class Meta:
        ordering = ['pk']
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    class Meta:
        ordering = ['pk']
    title = models.CharField(max_length=50)
    postpicture = models.FileField(upload_to='images/', null=True, verbose_name="")
    content = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    def __str__(self):
        return self.title + ' | ' + str(self.user)


    
class Comment(models.Model):
    class Meta:
      ordering = ['pk']
    body = models.TextField()
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=False)
#     class Meta: 
#         ordering = ('date_added',) 
       
    def __str__(self):
        return self.post.title 




