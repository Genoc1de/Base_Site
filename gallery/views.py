from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView, DetailView

from .models import Photo, Comment

def GalleryListView(request):
    photos = Photo.objects.all()
    context = {"photos": photos}
    return render(request, "gallery/gallery.html", context)


class GalleryUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['image_photo', 'description', 'date']
    template_name = 'gallery/gallery_edit.html'
    def get_success_url(self):

        return reverse_lazy('gallery_detail', kwargs={'pk': self.object.pk})

class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'gallery/gallery_del.html'
    success_url = reverse_lazy('gallery_list')


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

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "comment/new_comment.html"
    fields = ['text']
    def form_valid(self, form):
        form.instance.author = self.request.user
        photo = Photo.objects.get(pk=self.kwargs['pk'])  # Используйте 'pk' вместо 'photo_id'
        form.instance.photo = photo
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('gallery_detail', kwargs={'pk': self.kwargs['pk']})

class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comment/comment_delete.html"

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy('gallery_detail', kwargs={'pk': self.kwargs['photo_id']})

class CommentUpdateView(UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment/comment_edit.html'
    fields = ['text']

