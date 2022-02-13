from django.db import models

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
    postpicture = models.ImageField(upload_to='images/')
    content = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date = models.DateField()
    def __str__(self):
        return self.title + '|' + str(self.user)
    
class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# student_track = models.ForeignKey(Tracks, on_delete=models.CASCADE)

