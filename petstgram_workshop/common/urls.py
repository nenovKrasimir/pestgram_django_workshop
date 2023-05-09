from django.urls import path, include

from petstgram_workshop.common import views


urlpatterns = [
    path('', views.home_page, name='home-page')
]