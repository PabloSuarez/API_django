from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
