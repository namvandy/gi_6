from django.contrib.auth.models import User
from django.db import models
from projectapp.models import Project
# Create your models here.
# on_delete = CASCADE 유저가 없어진다면 구독정보도 다 사라지게



class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription', null=False)

    class Meta:
        unique_together = ['user','project']    # 하나의 사용자는 하나의 구독만 가능하게 옵션. 두 개를 묶어 하나로 만듬.