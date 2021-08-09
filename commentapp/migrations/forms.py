from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        #article, writer, created_at은 자동이니 받아올 것은 content만 받아오면 됨.
