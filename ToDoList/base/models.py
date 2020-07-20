from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class toDoPost(models.Model):
    content = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # priority=None

    def __str__(self):
        return self.content
