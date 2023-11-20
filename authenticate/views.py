import os
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from .forms import SignUpForm, EditProfileForm, ChangePasswordForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile, Element


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно авторизовались!')
            return redirect('home')
        else:
            messages.warning(request, "Некорректный логин или пароль!")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Вы вышли из аккаунта")
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile = Profile.objects.create(user=user)
            profile.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'authenticate/register.html', {'form': form})



def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Профиль успешно обновлен")
            return redirect('home')
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'authenticate/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Пароль успешно изменен")
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
        print(form)
    context = {
        'form': form,
    }
    return render(request, 'authenticate/change_password.html', context)

def profile(request):
    return render(request, 'pages/profile.html')

def maps(request):
    return render(request, 'pages/maps.html')

def home(request):
    elements = Element.objects.all()
    context = {"elements": elements}
    return render(request, "pages/home.html", context)

def game(request):
    return render(request, "pages/2048.html")

class ElementDetailView(DetailView):
    model = Element
    template_name = "element/element_detail.html"
    context_object_name = 'element'

class ElementDeleteView(LoginRequiredMixin, DeleteView):
    model = Element
    template_name = 'element/element_delete.html'
    success_url = reverse_lazy('home')

class ElementCreateView(LoginRequiredMixin, CreateView):
    model = Element
    template_name = "element/element_new.html"
    fields = ['title','text', 'image']
    login_url = 'login_user'
    success_url = reverse_lazy('home')

class ElementUpdateView(LoginRequiredMixin, UpdateView):
    model = Element
    fields = ['title','text', 'image']
    template_name = "element/element_edit.html"
    success_url = reverse_lazy('home')


