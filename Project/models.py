# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Project(models.Model):
    '''
    
    '''
class Direction(models.Model): 
    name=models.CharField(max_length=20)
    
class Image(models.Model):
    description=models.CharField(max_length=999)
    address=models.FilePathField()
    flag=models.BooleanField()#是否为标志
