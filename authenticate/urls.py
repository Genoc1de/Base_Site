from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.signup, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

    path('password_reset_form/', auth_views.PasswordResetView.as_view(),
         name='password_reset_form'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
    path('maps/', views.maps, name='maps'),
    path('gallery/', include('gallery.urls')),
    path('2048/', views.game, name='2048'),
    path('<int:pk>/', views.ElementDetailView.as_view(), name='element_detail'),
    path('<int:pk>/delete/', views.ElementDeleteView.as_view(), name='element_delete'),
    path('new/', views.ElementCreateView.as_view(), name='element_new'),
    path('<int:pk>/edit/', views.ElementUpdateView.as_view(), name='element_edit'),

]
