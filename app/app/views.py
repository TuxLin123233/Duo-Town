from django.http import HttpResponseRedirect

def page_url(target):
    website = f"http://localhost:8080/{target}/{target}.html"
    return website

# 页面跳转
def register(request):
    return HttpResponseRedirect(page_url('register'))