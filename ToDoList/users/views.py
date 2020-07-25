from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-login')
    else:
        form = UserRegisterForm()
    context = {
        'forms': form,
        'title': 'Register'
    }
    return render(request, 'users/register.html', context)


def login(request):
    context = {'title': 'Login'}
    return render(request, 'users/login.html', context)


def logout(request):
    context = {'title': 'Logout'}
    return render(request, 'users/logout.html', context)
