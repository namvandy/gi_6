from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World')
    if request.method == 'POST':

        temp = request.POST.get("input_text")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # hello_world_list = HelloWorld.objects.all()
        # return HttpResponseRedirect('accountapp:hello_world')
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # return render(request, 'accountapp/hello_world.html',
        #               context={'hello_world_list': hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})







#     Class Based View
class AccountCreateView(CreateView):
    model= User         #무엇을 만들지 #django에서 지원하는 기능 User
    form_class = UserCreationForm #django에서 지원하는 기능 UserCreationForm
    #두개가 존재, 비밀번호 입력창, 출력창
    success_url = reverse_lazy('accountapp:hello_world')
    #reverse를 바로쓰면안됨. _lazy를 쓰는이유는 실체 객체생성후 필요할 때 호출해야함. function base와 class base의 차이
    template_name = 'accountapp/create.html'
    #이 4개로 회원가입 로직 완성
