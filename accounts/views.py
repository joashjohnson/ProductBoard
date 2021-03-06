from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLogin,UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('index')
    context = {
        'form': form,
    }
    return  render(request,'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def create_view(request):
    return

def edit_view(request):
    return