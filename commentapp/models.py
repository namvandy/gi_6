from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)
    #1대 다의 관계 foreignkey설정
    writer = models.ForeignKey(User,on_delete=models.SET_NULL,
                               related_name='comment',null=True)
    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)