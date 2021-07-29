

from django.http import HttpResponseForbidden

from profileapp.models import Profile

#프로필 소유권 필요
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk']) #db에서 가져옴
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated
