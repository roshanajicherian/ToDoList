from . import models
from django.forms import ModelForm
from django import forms


class PostForm(ModelForm):
        class Meta:
            model = models.toDoPost
            fields = ['content', 'deadline']
