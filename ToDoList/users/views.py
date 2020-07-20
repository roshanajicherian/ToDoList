from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-home')
    else:
        form = UserRegisterForm()
    context = {
        'forms': form,
        'title': 'Register'
    }
    return render(request, 'users/register.html', context)
