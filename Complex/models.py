# -*- coding: utf-8 -*-
from django.db import models
from User.models import User
from New.models import New
from Project.models import Project
from Competition.models import Competition

# Create your models here.
Image_CHOICES ={
  ('User','个人头像'),   
  ('Competition','比赛图片'), 
  ('Project','项目图片'), 
  ('New','新闻图片'),           
}
class Image(models.Model):
    description=models.CharField(max_length=999)
    address=models.FilePathField()
    flag=models.BooleanField()#是否为标志
    type=models.CharField(choices=Image_CHOICES)#图片类型
    new_photo=models.ForeignKey(New,null=True)
    competition_photo=models.ForeignKey(Competition,null=True)
    user_photo=models.ForeignKey(User,null=True)
    project_photo=models.ForeignKey(Project,null=True)
    
Direction_CHOICES = (
    ('T', 'Type'),
    ('L', 'Language'),
)      
class Direction(models.Model): 
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=1,choices=Direction_CHOICES)
    
class Case(models.Model):
    time=models.DateTimeField()#事件发生时间
    description=models.CharField(max_length=999)#事件描述
    level=models.SmallIntegerField()#事件严重等级