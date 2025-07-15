import os.path

import django.db.utils
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from .models import User

"""获取csrf_token"""
@api_view(['GET'])
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf': csrf_token})

"""判断用户登录状态"""
@api_view(['GET'])
def check_session(request):
    user_id = request.session.get('user_id')    # 获取用户session
    if user_id is None:
        return JsonResponse({'message': 'not_logged_in'})
    else:
        return JsonResponse({'message': 'logged_in'})

"""添加用户"""
@api_view(["POST"])
@csrf_protect
def add_user(request):
    # 获取请求数据
    username = request.data.get('username')
    password = request.data.get('password')

    # 添加到数据库中
    try:
        if len(password) < 8:   # 密码长度太短
            return JsonResponse({'message': 'password_error'})
        else:   # 成功
            # 创建User对象
            User.objects.create(username=username, password=password)


    except django.db.utils.IntegrityError:
        # 试图注册一个已有的帐号
        return JsonResponse({'message': 'repeat'})

    # 返回结果
    return JsonResponse({'message': 'success'})

"""检查用户是否在数据库中"""
@api_view(['POST'])
@csrf_protect
def check_user(request):
    # 获取请求数据
    username = request.data.get('username')
    password = request.data.get('password')

    # 获取数据库里面的数据
    search_result = User.objects.filter(username=username).first()
    if search_result is None:   # 该用户还没注册
        return JsonResponse({'message': 'no_user'})
    elif password != search_result.password:    # 密码错误
        return JsonResponse({'message': 'password_error'})
    else:   # 都排除了错误, 登录成功
        request.session['user_id'] = search_result.id
        return JsonResponse({'message': 'success'})

"""获取用户信息"""
@api_view(['GET'])
@csrf_protect
def get_user(request):
    # 获取用户实例
    user_id = request.session.get('user_id')
    user = User.objects.filter(id=user_id).first()

    return JsonResponse({
        'id': user_id,
        'username': user.username,
        'gender': user.gender,
        'age': user.age,
        'fans': user.get_fans_length(),
        'likes': user.likes,
        'followers': user.get_following_length(),
        'friends': user.get_friends_length(),
        'headshot': user.headshot,
        'blogs': user.get_blogs_length()
    })

@api_view(['GET'])
@csrf_protect
def get_headshot(request, headshot_name):
    url = os.path.join('img/headshots', f'{headshot_name}.png')
    with open(url, 'rb') as f:
        image_data = f.read()

    return HttpResponse(image_data, content_type="image/png")
