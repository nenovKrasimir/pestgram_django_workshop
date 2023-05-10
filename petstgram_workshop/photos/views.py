from django.shortcuts import render


# Create your views here.


def add_photo(request):
    return render(request=request, template_name='photos/photo-add-page.html')


def edit_photo(request):
    pass
