from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

class Books(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    desciption=models.TextField()
    publish_date=models.DateField(default=timezone.now)
    price=models.DecimalField(decimal_places=2,max_digits=8)
    stock=models.IntegerField(default=0)