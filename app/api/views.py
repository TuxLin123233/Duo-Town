from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import User

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    new_user = User.objects.create(name=username, password=password)
    print(new_user)

    return JsonResponse({"status": "ok"})