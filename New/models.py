# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class New(models.Model):
    title=models.CharField(max_length=99)
    time=models.DateTimeField()
    content=models.CharField(max_length=999)
    author=models.CharField(max_length=10)
    times=models.IntegerField()

class Image(models.Model):
    description=models.CharField(max_length=999)
    address=models.FilePathField()
    flag=models.BooleanField()#是否为标志

class Case(models.Model):
    time=models.DateTimeField()#事件发生时间
    description=models.CharField(max_length=999)#事件描述
    level=models.SmallIntegerField()#事件严重等级



