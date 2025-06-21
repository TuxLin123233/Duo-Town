from django.urls import path

from .views import register
from .views import (login)
from .views import get_csrf_token

urlpatterns = [
    path('csrf', get_csrf_token),
    path('register', register),
    path('login', login)
]