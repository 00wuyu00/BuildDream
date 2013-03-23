# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class New(models.Model):
    title=models.CharField(max_length=99)
    time=models.DateTimeField()
    content=models.CharField(max_length=999)
    author=models.CharField(max_length=10)
    times=models.IntegerField()






