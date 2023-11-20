from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.GalleryListView, name='gallery_list'),
    path('<int:pk>/edit/', views.GalleryUpdateView.as_view(), name='gallery_edit'),
    path('new/', views.GalleryCreateView.as_view(), name='gallery_new'),
    path('<int:pk>/', views.GalleryDetailView.as_view(), name='gallery_detail'),
    path('comment/new/<int:pk>/', views.CommentCreateView.as_view(), name='comment_new'),
    path('gallery/comment/<int:photo_id>/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('<int:pk>/delete/', views.GalleryDeleteView.as_view(), name='gallery_del'),

]