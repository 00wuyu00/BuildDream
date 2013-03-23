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
    project_type=models.ManyToManyField(Direction)
    #Begin_time=models.DateTimeField() 先考虑可行性
    #End_time=models.DateTimeField()先考虑可行性
    description=models.CharField(max_length=999)
    #process_set 获得流程事件
    website=models.URLField()#比赛网址
    flag_process=models.BooleanField()