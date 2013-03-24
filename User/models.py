# -*- coding: utf-8 -*-
from django.db import models

    
# Create your models here.
 
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    grade=models.IntegerField(max_length=2)
    phone=models.CharField(max_length=11)
    student_id=models.CharField(max_length=14)
    good_direction=models.ManyToManyField('Direction',related_name="good_direction")
    follow_direction=models.ManyToManyField('Direction',related_name="follow_direction")
    introduction=models.CharField(max_length=100)
    
class Direction(models.Model): 
    name=models.CharField(max_length=20)
    
class Image(models.Model):
    description=models.CharField(max_length=999)
    address=models.FilePathField()
    flag=models.BooleanField()#是否为标志

    



    