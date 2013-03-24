from django.db import models

# Create your models here.
class Direction(models.Model): 
    name=models.CharField(max_length=20)