from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from django.urls import reverse
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required) # 로그인 여부 판단
class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user #요청유저
        project = Project.objects.get(pk=kwargs['project_pk'])
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete() # 구독정보가 존재하면 삭제 == 구독해제
        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):

        return reverse('projectapp:detail',kwargs={'pk': kwargs['project_pk']}) #구독게시판으로 넘어가게