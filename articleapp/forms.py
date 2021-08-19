from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','image','project' ,'content'] #클라이언트로부터 입력받을 것들