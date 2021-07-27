from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

# def form_invalid(self, form): 이건 검증과정이 실패 했을 때 실행이 되는 함수
    #검증 과정이 다 끝나고 나서 실행이 되는 함수
    # form이 가지고 있는 검증된 데이터의 instance
    # 클라이언트가 아닌 서버의 user에게 받음.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) #부모메서드의 form_valid를 가져옴.

class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'


