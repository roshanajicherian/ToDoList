from django.shortcuts import render
from .models import toDoPost

def Home(request):
    context = {
        'toDos': toDoPost.objects.all(),
        'title': 'Home'
    }
    return render(request, 'base/home.html', context)
