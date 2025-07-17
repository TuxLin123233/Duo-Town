from django.conf import settings
from django.urls import path
from .views import (
    get_csrf_token,
    add_user,
    check_user,
    check_session,
    get_user,
    get_headshot,
    add_blog,
    get_appreciation,
    get_headshot_list,
    get_background
)
from django.conf.urls.static import static

# 普通的GET方法
origin_GET = [
    path('csrf/', get_csrf_token),
    path('get_user/', get_user),
    path('check_session/', check_session),
    path('get_headshot_list/', get_headshot_list),
]

# 普通的POST方法
origin_POST = [
    path('add_user/', add_user),
    path('check_user/', check_user),
    path('add_blog/', add_blog),
]

# 图片相关方法
image_GET = [
    path('image/headshot/<str:headshot_name>', get_headshot),
    path('image/appreciate/', get_appreciation),
    path('image/background/', get_background)
]

urlpatterns = []
urlpatterns.extend(origin_GET)
urlpatterns.extend(origin_POST)
urlpatterns.extend(image_GET)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)