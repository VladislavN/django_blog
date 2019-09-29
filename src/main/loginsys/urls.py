import re
from django.contrib import admin
from django.urls import path, include
import loginsys.views

urlpatterns = [
    path('login/', loginsys.views.login),
    path('logout/', loginsys.views.logout),
]
