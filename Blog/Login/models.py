from datetime import datetime
from django.db import models
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('Login:home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    comment_text = models.CharField(max_length=400)
    commented_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.comment_text)

    def get_absolute_url(self):
        return reverse('Login:home')