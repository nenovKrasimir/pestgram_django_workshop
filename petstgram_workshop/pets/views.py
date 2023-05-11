from django.shortcuts import render


def pet_details(request, username, pet_name):
    return render(request=request, template_name='pets/pet-details-page.html')


def add_pet(request):
    return render(request=request, template_name='pets/pet-add-page.html')


def pet_delete(request, username, pet_name):
    return render(request=request, template_name='pets/pet-delete-page.html')


def pet_edit(request, username, pet_name):
    return render(request=request, template_name='pets/pet-edit-page.html')
