from django.shortcuts import render, redirect
from .models import toDoPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def Home(request):
    context = {
        'toDos': toDoPost.objects.filter(author=request.user),
        'title': 'Home'
    }
    return render(request, 'base/home.html', context)


@login_required
def addPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.author = request.user
            temp.save()
            return redirect('todo-home')
    context = {'form': form, 'title': 'Add'}
    return render(request, 'base/addPost.html', context)

class editToDo(LoginRequiredMixin,UpdateView):
    model=toDoPost
    fields=['content','deadline']
    template_name='base/addPost.html'
    context_object_name='toDo'