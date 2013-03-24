from django.db import models

# Create your models here.
Type_CHOICES=(
('T','Type'),
('L','Language')
)
class Direction(models.Model): 
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=1,choices=Type_CHOICES)
