# -*- coding: utf-8 -*-
from django.db import models
from Complex.models import Direction

# Create your models here.
Level_CHOICES=(
('a','院级'),
('s','校级'), 
('n','国家级'),
('w','世界级'),
)   
class Competition(models.Model):
    name=models.CharField(max_length=100)
    level=models.CharField(max_length=1,choices=Level_CHOICES)
    description=models.CharField(max_length=999,blank=True)
    #case_set 获得流程事件
    website=models.URLField(blank=True)#比赛网址
    direction=models.ManyToManyField(Direction)
    
class CompetitionCase(models.Model):
    time=models.DateTimeField()#事件发生时间
    description=models.CharField(max_length=999)#事件描述
    level=models.SmallIntegerField(default=0)#事件严重等级
    competition=models.ForeignKey(Competition)

class CompetitionImage(models.Model):
    description=models.CharField(max_length=999,blank=True)
    address=models.FilePathField()
    flag=models.BooleanField(default=False)#是否为标志
    competition=models.ForeignKey(Competition)
