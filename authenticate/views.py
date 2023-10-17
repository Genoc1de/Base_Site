from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.models import User
from .models import Post



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
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {
        'form': form,
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
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "pages/home.html", context)

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'pages/post_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['image_url','title', 'date_posted', ]
    template_name = 'post_edit.html'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['image_url','title', 'date_posted']
    login_url = 'login'