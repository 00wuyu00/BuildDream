# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class New(models.Model):
    title=models.CharField(max_length=99)
    time=models.DateTimeField(auto_now_add=True)
    content=models.CharField(max_length=999)
    author=models.CharField(max_length=10)
    times=models.IntegerField(default=0)

class NewImage(models.Model):
    description=models.CharField(max_length=999,blank=True)
    address=models.FilePathField()
    flag=models.BooleanField(default=False)#是否为标志
    new=models.ForeignKey(New)

class NewCase(models.Model):
    time=models.DateTimeField()#事件发生时间
    description=models.CharField(max_length=999)#事件描述
    level=models.SmallIntegerField(default=0)#事件严重等级
    new=models.ForeignKey(New)



