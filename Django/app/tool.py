from bs4 import BeautifulSoup

from app.models import User


def get_session_user(request):
    """
    从Session中获取用户
    :param request: 请求对象
    :return: 返回数据库用户实例
    """

    user_id = request.session.get('user_id')
    user = User.objects.filter(id=user_id).first()
    return user

def get_safety_text(*args):
    """
    判断文本是否为安全
    :param args: 多个文本
    :return: 返回结果
    """
    result = True
    for i in args:
        state = bool(BeautifulSoup(i).find())
        if state:
            result = False
            break

    # 返回结果
    return result