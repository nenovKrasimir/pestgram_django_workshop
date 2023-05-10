from django.contrib import admin

# Register your models here.
from petstgram_workshop.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(Pet, PetAdmin)
