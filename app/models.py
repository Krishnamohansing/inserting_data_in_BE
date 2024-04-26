from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)
    
    

class WebPage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(default='abc123@gmail.com')
    url=models.URLField()
    
    
class AccessRecord(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    author=models.CharField(max_length=100)