from django.urls import path, include

from petstgram_workshop.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.show_profile_details, name='show_profile')]