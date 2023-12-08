from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    tag_id = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    
class Setting(models.Model):
    name = models.CharField(max_length=100)
    tag_id = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

class Incident(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)
    stage = models.PositiveSmallIntegerField()
    time_stamp = models.DateTimeField(auto_now=True)
    
class ChatLog(models.Model):
    uid = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=10)
    content = models.CharField(max_length=5000)