from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=64)
    added = models.DateTimeField(auto_now_add=True)
