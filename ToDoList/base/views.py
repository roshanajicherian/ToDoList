from django.shortcuts import render, redirect
from .models import toDoPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class editToDo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = toDoPost
    fields = ['content', 'deadline']
    template_name = 'base/addPost.html'
    context_object_name = 'toDo'

    def is_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


class deleteToDo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = toDoPost
    template_name = 'base/delete_todo.html'
    context_object_name = 'toDo'
    success_url = '/'

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False
