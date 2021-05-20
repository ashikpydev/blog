from ast import AugLoad
from django.contrib.admin.decorators import register
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form, 'registered':registered}
    return render(request, "signup.html", dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username =username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'login.html', context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance = current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance = current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance = current_user)

    return render(request, 'change_profile.html', context={'form':form})

@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data = request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'change_pass.html', context = {'form':form, 'changed':changed})

@login_required
def add_pro_pic(request, *args, **kwargs):
    form = ProfilePic(request.POST or None)
    # if request.method == 'POST':
    #     print('req paichi')
    #     form = ProfilePic(request.POST, request.FILES)
    #     print('file e dhukte perechi')
    if form.is_valid():

        user_obj = form.save(commit=False)

        user_obj.user = request.user

        user_obj.save()
        return redirect('/')
    context = {
        'form':form
        }
    return render(request, 'add_pic.html', context)