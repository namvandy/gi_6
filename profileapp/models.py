from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#on_delete(삭제 되었을 때) (CASCADE:종속) User삭제 시 종속적으로 같이 삭제를 하겠다.
#on_delete=models.SET_NULL은 User가 누군지 모르고 NULL인 상태로 하겠다.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile') #1대1 연결모델 #django에서 제공하는 User를 가져옴

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)