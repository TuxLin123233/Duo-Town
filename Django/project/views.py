from rest_framework.decorators import api_view
from django.shortcuts import redirect


@api_view(['GET'])
def welcome(request):
    return redirect("http://localhost:8080/pages/register/register.html")