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
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    stage = models.PositiveSmallIntegerField()
    time_stamp = models.DateTimeField()
    stage_name = ""
    finished = []