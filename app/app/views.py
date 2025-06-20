from django.http import HttpResponseRedirect


def register(request):
    return HttpResponseRedirect("http://localhost:8080/pages/register/register.html")