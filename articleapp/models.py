from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    #models.SET_NULL:작성자 미상의 글로 남기겠다
    title = models.CharField(max_length=300, null=True) #null=True:타이틀이 없어도 된다.
    image = models.ImageField(upload_to='article/',null=True)
    content = models.TextField(null=True) #긴 문자열은 CharFiled말고 TextField로 지정

    created_at = models.DateField(auto_now_add=True,null=True)
    #게시글 작성된 시간, 자동으로 시간지정
