from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def render_register_form(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        # return HttpResponse("Form submitted successfully!")
        return redirect("/blog/login")
    else:
        return render(request, "auth/register.html")


def render_login_form(request):
    if request.method == "POST":
        # Handle form submission and user login logic here
        print("Form submitted")
    else:
        return render(request, "auth/login.html")
