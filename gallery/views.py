from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView, DetailView

from .models import Photo

def GalleryListView(request):
    photos = Photo.objects.all()
    context = {"photos": photos}
    return render(request, "gallery/gallery.html", context)


class GalleryUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['image_photo', 'description', 'date']
    template_name = 'gallery/'
    success_url = reverse_lazy('home')

class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'gallery/'
    success_url = reverse_lazy('home')


class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = "gallery/new_gallery.html"
    fields = ['image_photo','description', 'date']
    login_url = 'login_user'
    success_url = reverse_lazy('gallery_list')

class GalleryDetailView(DetailView):
    model = Photo
    template_name = "gallery/gallery_detail.html"
    context_object_name = 'photo'
