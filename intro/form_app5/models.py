from django.db import models


class Message(models.Model):

    CHOICES = [
        (0, "Pytanie"),
        (1, "Inne")
    ]

    name = models.CharField(max_length=64)
    email = models.EmailField()
    category = models.IntegerField(choices=CHOICES)
    subject = models.CharField(max_length=64)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
