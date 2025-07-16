from app.models import User


# 从Session中获取用户
def get_session_user(request):
    user_id = request.session.get('user_id')
    user = User.objects.filter(id=user_id).first()
    return user