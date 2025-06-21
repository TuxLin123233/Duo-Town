from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework.decorators import api_view

from .models import User

@ensure_csrf_cookie
def get_csrf_token(request):
    # 返回一个JSON响应，同时在浏览器设置CSRF_TOKEN
    return JsonResponse({'status': 'CSRF Token Set'})


@api_view(['POST'])
@csrf_protect
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # 获取用户
    search_user = User.objects.filter(username=username)
    if search_user.exists():  # 存在该用户
        print("repeat")
        return JsonResponse({'message': 'repeat_username'})
    else:   # 不存在该用户
        # 如果密码长度 < 6
        if len(password) < 6:
            return JsonResponse({'message': 'short_password'})
        else:
            request.session['username'] = username

            return JsonResponse({'message': 'ok'})


@api_view(['POST'])
def login(request):
    username = request.data.get('username')

    # 搜索到的数据库结果
    user_data = User.objects.get(username=username)
    print(user_data)