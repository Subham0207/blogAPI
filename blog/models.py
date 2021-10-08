from django.db import models
from datetime import datetime


# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=50)
    img_author = models.ImageField()
    img_blog = models.ImageField()
    views = models.IntegerField(default=0)
    body = models.TextField()
    tags = models.TextField(default="None")

    def __str__(self):
        return self.author



