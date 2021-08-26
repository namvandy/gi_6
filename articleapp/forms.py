from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style':'min-height: 10rem;'
                                                                    'text-align:left;'}))

    #content=문자열을 입력받을 수 있는 형태, 클래스는 editable / attrs로 미리 html을 지정
    class Meta:
        model = Article
        fields = ['title','image','project' ,'content'] #클라이언트로부터 입력받을 것들