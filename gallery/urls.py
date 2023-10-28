from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.GalleryListView, name='gallery_list'),
    path('<int:pk>/edit/', views.GalleryUpdateView.as_view(), name='galleryedit'),
    path('<int:pk>/delete/', views.GalleryDeleteView.as_view(), name='gallery_delete'),
    path('new/', views.GalleryCreateView.as_view(), name='gallery_new'),
    path('<int:pk>/', views.GalleryDetailView.as_view(), name='gallery_detail'),
]