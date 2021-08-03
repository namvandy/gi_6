from django.shortcuts import render

# Create your views here.

#CRUD모두 사용(게시판)
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from django.urls import reverse

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user #request를 보내는 user로 writer를 할당
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'
    # success_url = reverse_lazy('articleapp:list')
    #동적으로 url지정
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})