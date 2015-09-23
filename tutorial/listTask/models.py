from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
