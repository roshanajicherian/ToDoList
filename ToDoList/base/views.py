from django.shortcuts import render, redirect
from .models import toDoPost
from .forms import PostForm


def Home(request):
    context = {
        'toDos': toDoPost.objects.all(),
        'title': 'Home'
    }
    return render(request, 'base/home.html', context)


def addPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-home')
    context = {'form': form, 'title': 'Add'}
    return render(request, 'base/addPost.html', context)
