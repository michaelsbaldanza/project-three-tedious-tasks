from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=100)
    time = models.IntegerField
    person = models.CharField(max_length=100)