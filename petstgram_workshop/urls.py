
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstgram_workshop.common.urls')),
    path('photos/', include('petstgram_workshop.photos.urls')),
    path('pets/', include('petstgram_workshop.pets.urls')),
    path('accounts/', include('petstgram_workshop.accounts.urls'))

]
