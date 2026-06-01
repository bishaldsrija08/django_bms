from django.urls import path

from .views import render_register_form
from .views import render_login_form

urlpatterns =[
    path('register', render_register_form, name='register'),
    path('login', render_login_form, name='login')
]