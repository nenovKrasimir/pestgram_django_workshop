from django.shortcuts import render


# Create your views here.

def add_pet(request):
    return render(request=request, template_name='pets/pet-add-page.html')


def pet_delete(request):
    pass


def pet_edit(request):
    pass
