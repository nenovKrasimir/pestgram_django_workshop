from django.shortcuts import render


# Create your views here.

def register(request):
    return render(request=request, template_name='accounts/register-page.html')


def login(request):
    return render(request=request, template_name='accounts/login-page.html')


def show_profile_details(request):
    return render(request=request, template_name='accounts/profile-details-page.html')


def edit_profile(request):
    pass


def delete_profile(request):
    pass
