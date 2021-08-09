from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DeleteView

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from django.urls import reverse

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    def get_success_url(self):

        return reverse('articleapp:detail',kwargs={'pk':self.object.article.pk})

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)

class CommentDeleteView(DeleteView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/delete.html'