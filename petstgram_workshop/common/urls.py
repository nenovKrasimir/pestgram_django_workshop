from django.urls import path, include

from petstgram_workshop.common import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('like/<int:photo_id>/', views.like_functionality, name="like"),
    path('share/<int:photo_id>/', views.copy_link_to_clipboard, name='share')]