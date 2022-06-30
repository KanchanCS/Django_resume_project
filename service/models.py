from django.db import models

# Create your models here.
class Service(models.Model):
    icon=models.CharField(max_length=100)
    heading=models.CharField(max_length=100)
    discription=models.TextField()