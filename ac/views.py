from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm
# Create your views here.


def login(request):

    if request.user.is_authenticated: #이미로그인됨
        return redirect('po:index')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'po:index')
        
    else:
        form = CustomAuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'ac/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('po:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('po:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }

    return render(request, 'ac/signup.html', context)