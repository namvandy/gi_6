from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk']) #DB에 접속해서 유저의 정보를 가져옴 #입력받은 pk의 정보로 접근
        if target_user == request.user:
            return func(request, *args,**kwargs)
        else:
            return HttpResponseForbidden()
    return decorated #호출 '()'이 아닌 함수 자체를 반환


