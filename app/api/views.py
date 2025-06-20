from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import User

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    # 检查该用户是否在数据库中
    search_result:bool = User.objects.filter(username=username).exists()
    if search_result:  # 存在该用户
        return JsonResponse({"status": "repeat"})
    else:   # 不存在该用户
        return JsonResponse({"status": "ok"})


@api_view(['POST'])
def login(request):
    username = request.data.get('username')

    # 搜索到的数据库结果
    user_data = User.objects.get(username=username)
    print(user_data)