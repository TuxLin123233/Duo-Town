import django.db.utils
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from .models import User

"""获取csrf_token"""
@api_view(['GET'])
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf': csrf_token})

# 添加用户
@api_view(["POST"])
@csrf_protect
def add_user(request):
    # 获取请求数据
    username = request.data.get('username')
    password = request.data.get('password')

    # 添加到数据库中
    try:
        if len(password) < 8:   # 密码长度太短
            return JsonResponse({'status': 'password_error'})
        else:   # 成功
            User.objects.create(username=username, password=password)
    except django.db.utils.IntegrityError:
        # 试图注册一个已有的帐号
        return JsonResponse({'status': 'repeat'})

    # 返回结果
    return JsonResponse({'status': 200})

@api_view(['POST'])
def check_user(request):
    # 获取请求数据
    username = request.data.get('username')
    password = request.data.get('password')

    # 获取数据库里面的数据
    search_result = User.objects.filter(username=username).first()
    if search_result is None:   # 该用户还没注册
        return JsonResponse({'status': 'no_user'})
    elif password != search_result.password:    # 密码错误
        return JsonResponse({'status': 'password_error'})
    else:   # 都排除了错误, 登录成功
        return JsonResponse({'status': 200})