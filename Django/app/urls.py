from django.conf import settings
from django.urls import path
from .views import (
    get_csrf_token,
    add_user,
    check_user,
    check_session,
    get_user,
    get_headshot
)
from django.conf.urls.static import static

urlpatterns = [
    path('csrf/', get_csrf_token),
    path('add_user/', add_user),
    path('check_user/', check_user),
    path('check_session/', check_session),
    path('get_user/', get_user),
    path('image/headshot/<str:headshot_name>', get_headshot)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)