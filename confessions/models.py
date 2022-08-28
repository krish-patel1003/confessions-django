from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Confession(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    confession = models.CharField(max_length=280)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "@"+self.author.username + ": " + self.confession
    
    def get_absolute_url(self):
        return reverse('confessions-home')