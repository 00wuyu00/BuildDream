# -*- coding: utf-8 -*-
from django.db import models
from User.models import User
from Complex.models import Direction

# Create your models here.
class Question(models.Model):
    content=models.CharField(max_length=999)
    time=models.DateTimeField(auto_now_add=True)
    owner=models.ManyToManyField(User,related_name='owner')
    direction=models.ManyToManyField(Direction)
    comment_user=models.ManyToManyField(User,through='QuestionComment')
    
class QuestionComment(models.Model):
    content=models.CharField(max_length=999)
    time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User)
    question=models.ForeignKey(Question)