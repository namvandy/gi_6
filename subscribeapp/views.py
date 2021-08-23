from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView
from django.urls import reverse

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, 'get') # 로그인 여부 판단
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

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    def get_queryset(self):
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')    #Subscription에 project와 db를 연결해놓았음 / 유저가 보유하고 있는 구독한 project만 리스트화해 담음.
        article_list = Article.objects.filter(project__in=project_list)
        return article_list

