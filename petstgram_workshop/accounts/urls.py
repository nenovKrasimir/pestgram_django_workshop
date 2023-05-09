from django.urls import path, include

from petstgram_workshop.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>', include([
        path('', views.show_profile_details, name='profile-details'),
        path('edit/', views.edit_profile, name='edit-profile'),
        path('delete/', views.delete_profile, name='delete-profile')
    ]))
]
