from . import models
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = models.toDoPost
        fields = '__all__'
