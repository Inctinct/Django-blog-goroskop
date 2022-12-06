from django.db import models
from django.utils import timezone
# Create your models here.


class Goroskop(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(default='text')
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
