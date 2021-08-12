from django.db import models
from django.shortcuts import render

# Create your views here.

class Project(models.Model):
    name = models.CharField(max_length=20,null=False)
    description = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)
