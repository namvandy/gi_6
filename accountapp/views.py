from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld
from articleapp.models import Article

#     Class Based View
class AccountCreateView(CreateView):
    model= User         #무엇을 만들지 #django에서 지원하는 기능 User
    form_class = UserCreationForm #django에서 지원하는 기능 UserCreationForm
    #두개가 존재, 비밀번호 입력창, 출력창
    success_url = reverse_lazy('articleapp:list')
    #만들었을 때의 주소 지정
    #reverse를 바로쓰면안됨. _lazy를 쓰는이유는 실체 객체생성후 필요할 때 호출해야함. function base와 class base의 차이
    template_name = 'accountapp/create.html'
    #이 4개로 회원가입 로직 완성
#C
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,**kwargs)
#R

has_ownership = [login_required, account_ownership_required]


# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post') #이렇게 리스트로 만들면 위내용 decorate미사용 가능
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'

    template_name = 'accountapp/update.html'

    # def get(self, request,*args, **kwargs):
    #     # return super().get(request,*args, **kwargs)#부모메서드 호출 #부모클래스와 완전똑같음(여기까지 작성시),작성안한거나 마찬가지
    #     if request.user.is_authenticated and self.get_object()==request.user:
    #         return super().get(request, *args, **kwargs) #로그인이 되어있으면 실행
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)  # 로그인이 되어있으면 실행
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden
    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.object.pk})

# U
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'

    # def get(self, request, *args, **kwargs):
    #     # return super().get(request,*args, **kwargs)#부모메서드 호출 #부모클래스와 완전똑같음(여기까지 작성시),작성안한거나 마찬가지
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request, *args, **kwargs)  # 로그인이 되어있으면 실행
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)  # 로그인이 되어있으면 실행
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden