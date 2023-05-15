from django.shortcuts import render, redirect

from petstgram_workshop.pets.forms import PetForm, PetDeleteForm
from petstgram_workshop.pets.models import Pet


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        "pet": pet,
        "all_photos": all_photos,

    }
    return render(request=request, template_name='pets/pet-details-page.html', context=context)


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {'form': form}
    return render(request=request, template_name='pets/pet-add-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('show_profile', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}
    return render(request=request, template_name='pets/pet-delete-page.html', context=context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)
    context = {"form": form}
    return render(request=request, template_name='pets/pet-edit-page.html', context=context)
