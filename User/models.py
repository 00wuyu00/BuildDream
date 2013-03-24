# -*- coding: utf-8 -*-
from django.db import models
from Complex.models import Direction
from django.contrib.auth.models import User

    
# Create your models here.
 
class UserInf(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    grade=models.IntegerField(max_length=2)
    phone=models.CharField(max_length=11,blank=True)
    student_id=models.CharField(max_length=14)
    good_direction=models.ManyToManyField(Direction,related_name="good_direction")
    follow_direction=models.ManyToManyField(Direction,related_name="follow_direction")
    introduction=models.CharField(max_length=100,blank=True)
    user=models.OneToOneField(User)   
    
class UserImage(models.Model):
    description=models.CharField(max_length=999,blank=True)
    address=models.FilePathField()
    flag=models.BooleanField(default=False)#是否为标志
    user=models.ForeignKey(User)

    



    