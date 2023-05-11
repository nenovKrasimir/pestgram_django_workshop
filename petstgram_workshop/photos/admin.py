from django.contrib import admin

from petstgram_workshop.photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "date_of_publication", "description", "get_tagged_pets")

    @staticmethod
    def get_tagged_pets(obj):
        return ", ".join([pet.name for pet in obj.tagged_pets.all()])


admin.site.register(Photo, PhotoAdmin)