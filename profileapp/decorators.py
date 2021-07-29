

from django.http import HttpResponseForbidden

from profileapp.models import Profile

#프로필 소유권 필요하다
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])   #db에서가져옴
        if target_profile.user == request.user: #user가 일치하는지
            func(request,*args,**kwargs) #실행시키려는 인자를 받아서 실행
        else:
            return HttpResponseForbidden()
    return decorated