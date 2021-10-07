from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=100)
    date = now
    author = models.CharField(max_length=50)
    img_author = models.ImageField()
    img_blog = models.ImageField()
    views = models.IntegerField(default=0)
    body = models.TextField()

    def __str__(self):
        return self.author



