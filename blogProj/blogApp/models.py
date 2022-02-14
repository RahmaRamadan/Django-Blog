from django.db import models
from datetime import datetime, date
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
class Category(models.Model):
    name = models.CharField(max_length=50)
    followers = models.ManyToManyField(User)
    def __str__(self):
        return self.name 
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    postpicture = models.FileField(upload_to='images/', null=True, verbose_name="")
    content = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title + ' | ' + str(self.user)


    
class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=False)
    class Meta: 
        ordering = ('date_added',) 

    def __str__(self):
        return self.post.title 

# student_track = models.ForeignKey(Tracks, on_delete=models.CASCADE)

