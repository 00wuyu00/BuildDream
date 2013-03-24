# -*- coding: utf-8 -*-
from django.db import models
from User.models import User
from Complex.models import Direction

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=999)
    start_time=models.DateField()
    end_time=models.DateField()
    owner=models.ForeignKey(User)
    join_user=models.ManyToManyField(User,related_name='join_user',blank=True)
    comment_user=models.ManyToManyField(User,through='ProjectComment',related_name='comment_user',blank=True)
    direction=models.ManyToManyField(Direction)
    
class ProjectImage(models.Model):
    description=models.CharField(max_length=999,blank=True)
    address=models.FilePathField()
    flag=models.BooleanField(default=False)#是否为标志
    project=models.ForeignKey(Project)
    
class ProjectComment(models.Model):
    content=models.CharField(max_length=999)
    time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User)
    question=models.ForeignKey(Project)
