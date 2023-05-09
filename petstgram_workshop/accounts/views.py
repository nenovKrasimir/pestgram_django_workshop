from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request=request, template_name='accounts/register-page.html')

def login(request):
    pass

def show_profile_details(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass