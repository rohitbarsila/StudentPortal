from django.db import models

# Create your models here.
class data(models.Model):
    Name=models.CharField(max_length=36,blank=False)
    Email=models.CharField(max_length=50,blank=False)
    Course=models.TextField(max_length=20,blank= False)
    Sem=models.TextField(max_length=10,blank=False)
    Subjects=models.TextField(max_length=100,blank=False)
    Query=models.TextField(blank=False)
