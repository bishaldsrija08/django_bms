from urllib import request

from django.shortcuts import render

# Create your views here.

def render_register_form(request):
    return render(request, 'auth/register.html')

def render_login_form(request):
    return render(request, 'auth/login.html')