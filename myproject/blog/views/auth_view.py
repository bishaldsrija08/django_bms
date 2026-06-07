from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages

def render_register_form(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect("/blog/login")
    else:
        return render(request, "auth/register.html")


def render_login_form(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            messages.success(request, "Login successful")
            return redirect("/blog/")
        else:
            messages.error(request, "Invalid email or password")
            return render(request, "auth/login.html")
        
    else:
        return render(request, "auth/login.html")