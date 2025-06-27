from django.urls import path
from .views import (
    get_csrf_token,
    add_user,
    check_user
)

urlpatterns = [
    path('csrf', get_csrf_token),
    path('add_user', add_user),
    path('check_user', check_user)
]