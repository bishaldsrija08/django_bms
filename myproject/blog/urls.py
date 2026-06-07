from django.urls import path

from .views.auth_view import render_login_form, render_register_form
from .views.home_view import render_homepage

urlpatterns =[  
    path('register', render_register_form, name='register'),
    path('login', render_login_form, name='login'),
    path('', render_homepage, name='home')
]