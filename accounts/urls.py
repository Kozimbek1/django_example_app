from django.contrib import admin
from django.urls import path

from accounts.views import post_login, registration

urlpatterns = [
    path('login/', post_login),
    path('', registration)
]