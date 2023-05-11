from django.urls import path, include

from petstgram_workshop.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.details_photo, name='photo-details'),
        path('edit/', views.edit_photo, name='photo-edit')
    ]))
]